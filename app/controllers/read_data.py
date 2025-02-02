from constants.run_status import RUN_STATUS
from utils.general_utils import get_json
from constants import values


def get_task_statuses(dag_data: dict, task: str) -> list:
    last_runs = [RUN_STATUS.EMPTY] * values.RUNS_DISPLAY_NUM
    if len(dag_data.keys()) == 0:
        return last_runs
    for i, key in enumerate(dag_data.keys()):
        if i == values.RUNS_DISPLAY_NUM:
            break
        last_runs[i] = RUN_STATUS.colors.get(dag_data[key]['tasks'][task]['status'])
    return last_runs


def sort_runs_by_scheduled_date() -> list:
    pass


def merge_data(meta_data: dict, dag_runs: dict) -> dict:
    displayed_data = {}
    for key in meta_data.keys():
        displayed_data[key] = {}
        for task in meta_data[key]:
            displayed_data[key][task] = get_task_statuses(dag_runs[key], task)
    return displayed_data


def fetch_dashboard_data():
    meta_data = get_json(values.META_DATA)['workflows']
    dag_runs = get_json(values.RUNS_DATA)
    return merge_data(meta_data, dag_runs)
