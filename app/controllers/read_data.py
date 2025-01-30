from utils.general_utils import get_json
from constants import values


def get_task_statuses(dag_data: dict, task: str, num_last_runs=5) -> list:
    last_runs = [None] * num_last_runs
    if len(dag_data.keys()) == 0:
        return last_runs
    for i, key in enumerate(dag_data.keys()):
        last_runs[i] = (dag_data[key]['tasks'][task]['status'])
    return last_runs


def merge_data(meta_data: dict, dag_runs: dict) -> dict:
    displayed_data = {}
    for key in meta_data.keys():
        displayed_data[key] = {}
        for task in meta_data[key]:
            displayed_data[key][task] = get_task_statuses(dag_runs[key], task)
    print(displayed_data)
    return displayed_data


def fetch_dashboard_data():
    meta_data = get_json(values.META_DATA)['workflows']
    dag_runs = get_json(values.RUNS_DATA)
    return merge_data(meta_data, dag_runs)
