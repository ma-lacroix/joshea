import json
import os

from controllers.validator import validate_dag, parse_dag_file
from utils.general_utils import read_configuration, get_meta_data, write_meta_data


def write_dag_to_db(new_dags_meta_data: list):
    meta_data = get_meta_data()
    for dag in new_dags_meta_data:
        meta_data['workflows'][dag.name] = dag.tasks
    write_meta_data(meta_data)


def fetch_workflow_meta_data() -> list:
    return get_meta_data()['workflows'].keys()


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
        return json.dumps({"Nothing new": ''})
    dags_to_add = get_list_valid_dags(new_dags)
    write_dag_to_db(dags_to_add)
    return prepare_create_response([dag.turn_into_dict() for dag in dags_to_add])
