from app.constants.run_status import RUN_STATUS
from app.utils.general_utils import get_json
from app.constants import values


def get_task_statuses(dag_data: list, task: str) -> list:
    last_runs = [RUN_STATUS.EMPTY] * values.RUNS_DISPLAY_NUM
    if len(dag_data) == 0:
        return last_runs
    for i, run in enumerate(dag_data):
        if i == values.RUNS_DISPLAY_NUM:
            break
        last_runs[i] = RUN_STATUS.colors.get(run['tasks'][task]['status'])
    return last_runs


def sort_runs_by_scheduled_date(dag_runs: dict) -> list:
    return [dag_runs[key] for key in sorted(dag_runs.keys())]


def merge_data(meta_data: dict, dag_runs: dict) -> dict:
    """
    Prepares the object that will be displayed by the frontend
    """
    displayed_data = {}
    for key in meta_data.keys():
        if meta_data[key] == RUN_STATUS.DELETED:
            continue
        displayed_data[key] = {}
        sorted_runs = sort_runs_by_scheduled_date(dag_runs[key])
        for task in meta_data[key]:
            displayed_data[key][task] = get_task_statuses(sorted_runs, task)
    return displayed_data


def fetch_dashboard_data():
    """
    Returns the object that will be displayed by the frontend
    """
    meta_data = get_json(values.META_DATA)['workflows']
    dag_runs = get_json(values.RUNS_DATA)
    return merge_data(meta_data, dag_runs)


def fetch_next_run(dag_name: str):
    """
    Returns the next scheduled run
    """
    dag_runs = get_json(values.RUNS_DATA).get(dag_name, "")
    if len(dag_runs) == 0:
        return {"dag_name": f"{dag_name}", "next_run": f"DAG does not exist"}
    sorted_keys = sorted(dag_runs.keys())
    for key in sorted_keys:
        if dag_runs.get(key)['status'] == RUN_STATUS.PENDING:
            return {"dag_name": f"{dag_name}", "next_run": f"{key}"}
    return {"dag_name": f"{dag_name}", "next_run": f"No scheduled next runs"}
