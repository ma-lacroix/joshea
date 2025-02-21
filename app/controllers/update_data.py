import datetime
import importlib
from time import sleep

from app.constants.run_status import RUN_STATUS
from app.utils.general_utils import write_json, get_json
from app.constants import values


def fetch_workflow_task_names(dag_name: str) -> list:
    return get_json(values.META_DATA)['workflows'][f"{dag_name}"]


def update_dag_task_run_status(dag_name: str, task_name: str, id: str, new_status: RUN_STATUS, top_level=False) -> bool:
    """
    Updates the DAG's run data. When set to True, the top_level parameter overwrites the DAG's overall status.
    """
    runs_data = get_json(values.RUNS_DATA)
    runs_data[dag_name][id]['tasks'][task_name]['status'] = new_status
    if top_level:
        runs_data[dag_name][id]['status'] = new_status
    write_json(runs_data, values.RUNS_DATA)
    return True


def validate_dag_execution_request(dag_name: str, id: str) -> bool:
    """
    Checks if the DAG execution request is valid
    """
    return bool(get_json(values.RUNS_DATA).get(dag_name, {}).get(id) is not None)


def execute_dag(dag_name: str, id: str) -> dict:
    print(f"{dag_name} - {id}")
    if not validate_dag_execution_request(dag_name, id):
        return {'status': RUN_STATUS.FAILED, 'message': 'Run ID does not exist'}
    task_names = fetch_workflow_task_names(dag_name)
    for i, task in enumerate(task_names):
        retries = 0
        while retries < values.RETRIES:
            try:
                if update_dag_task_run_status(dag_name, task, id, RUN_STATUS.RUNNING):
                    execute_dag_task(dag_name, task)
                else:
                    print(f"Failed to update task to {RUN_STATUS.RUNNING}")
                if update_dag_task_run_status(dag_name, task, id, RUN_STATUS.SUCCESS, i == len(task_names) - 1):
                    sleep(2)
                    break
                else:
                    print(f"Failed to update task to {RUN_STATUS.SUCCESS}")
            except Exception as e:
                print(f"Failed task {task} from {dag_name}: {e}")
                update_dag_task_run_status(dag_name, task, id, RUN_STATUS.PENDING)
                retries += 1
                if retries == values.RETRIES:
                    update_dag_task_run_status(dag_name, task, id, RUN_STATUS.FAILED, top_level=True)
                    return {'status': RUN_STATUS.FAILED, 'completed': datetime.datetime
                        .now().strftime('%Y-%m-%d %H:%M:%S')}
    return {'status': RUN_STATUS.SUCCESS, 'completed': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}


def execute_dag_task(dag_name: str, task_name: str) -> None:
    module = importlib.import_module(f"app.dags.{dag_name.replace('.py', '')}")
    func = getattr(module, task_name)
    func()
