import datetime
import json
import os
from uuid import uuid4

from app.constants import values
from app.constants.run_status import RUN_STATUS
from app.controllers.validator import validate_dag, parse_dag_file
from app.models.run_meta_data import DagRunMetaData
from app.models.task_run_meta_data import TaskRunMetaData
from app.utils.general_utils import read_configuration, get_json, write_json


def write_dag_meta_data_to_db(new_dags_meta_data: list):
    meta_data = get_json(values.META_DATA)
    for dag in new_dags_meta_data:
        meta_data['workflows'][dag.name] = dag.tasks
    write_json(meta_data, values.META_DATA)


def write_dag_names_run_data_to_db(new_dags_meta_data: list):
    runs_data = get_json(values.RUNS_DATA)
    for dag in new_dags_meta_data:
        runs_data[dag.name] = {}
    write_json(runs_data, values.RUNS_DATA)


def add_new_dag_run_to_db(dag_run: dict, dag_name: str, id: str):
    runs_data = get_json(values.RUNS_DATA)
    runs_data[dag_name][id] = dag_run
    write_json(runs_data, values.RUNS_DATA)


def fetch_workflow_meta_data() -> list:
    return get_json(values.META_DATA)['workflows'].keys()


def parse_folder() -> list:
    folder = read_configuration('dag_files_location')
    return os.listdir(folder)


def prepare_create_response(dags: list) -> dict:
    response = {}
    for dag in dags:
        response[dag['name']] = dag['tasks']
    return response


def get_list_valid_dags(new_dags: list) -> list:
    dags_to_add = []
    for dag in new_dags:
        if validate_dag(dag):
            dags_to_add.append(parse_dag_file(dag))
    return dags_to_add


def execute_create() -> json:
    existing_dags = fetch_workflow_meta_data()
    current_dags = parse_folder()
    new_dags = list(set(current_dags) - set(existing_dags))
    if len(new_dags) == 0:
        return {"message": 'nothing new'}
    dags_to_add = get_list_valid_dags(new_dags)
    write_dag_meta_data_to_db(dags_to_add)
    write_dag_names_run_data_to_db(dags_to_add)
    return prepare_create_response([dag.turn_into_dict() for dag in dags_to_add])


def validate_new_dag_run_request(request_body: dict) -> bool:
    return request_body.get("name", "_") in fetch_workflow_meta_data()


def schedule_dag_run(request_body: dict) -> json:
    if not validate_new_dag_run_request(request_body):
        return {f"Invalid POST request, missing key {request_body.get('name', '_')}"}
    task_names = get_json(values.META_DATA)['workflows'][request_body.get("name")]
    tasks = {}
    for task in task_names:
        tasks[task] = TaskRunMetaData(id=str(uuid4()),
                                      status=RUN_STATUS.PENDING,
                                      total_run_time=0)
    run = DagRunMetaData(status=RUN_STATUS.PENDING,
                         tasks=tasks)
    add_new_dag_run_to_db(run.turn_into_dict(), request_body.get("name"),
                          datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return run
