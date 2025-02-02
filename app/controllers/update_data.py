import datetime
import importlib
from time import sleep

from constants.run_status import RUN_STATUS
from utils.general_utils import write_json, get_json
from constants import values


def flush_meta_data() -> str:
    write_json({'workflows': {}}, values.META_DATA)
    write_json({}, values.RUNS_DATA)
    return "Meta data reset"


def fetch_workflow_task_names(dag_name: str) -> list:
    return get_json(values.META_DATA)['workflows'][f"{dag_name}"]


def update_dag_run_status(dag_name: str, task_name: str, id: str, new_status: RUN_STATUS) -> None:
    runs_data = get_json(values.RUNS_DATA)
    runs_data[dag_name][id]['tasks'][task_name]['status'] = new_status
    write_json(runs_data, values.RUNS_DATA)


def execute_dag(dag_name: str, id: str) -> dict:
    print(f"Executing {id}")
    task_names = fetch_workflow_task_names(dag_name)
    for task in task_names:
        try:
            update_dag_run_status(dag_name, task, id, RUN_STATUS.RUNNING)
            sleep(5)
            execute_dag_task(dag_name, task)
            sleep(5)
            update_dag_run_status(dag_name, task, id, RUN_STATUS.SUCCESS)
        except Exception as e:
            print(f"Failed task {task} from {dag_name}: {e}")
            update_dag_run_status(dag_name, task, id, RUN_STATUS.FAILED)
        sleep(2)
    return {'status': RUN_STATUS.SUCCESS, 'completed': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}


def execute_dag_task(dag_name: str, task_name: str) -> None:
    module = importlib.import_module(f"dags.{dag_name.replace('.py','')}")
    func = getattr(module, task_name)
    func()
