import json

from constants import values


def read_configuration(key: str):
    try:
        with open(f"{values.CONFIGURATION}", 'r') as file:
            conf = json.load(file)
        file.close()
        return conf[key]
    except FileNotFoundError:
        raise


def get_json(file_name: str) -> dict:
    try:
        with open(f"{file_name}", 'r') as file:
            meta_data = json.load(file)
        file.close()
        return meta_data
    except FileNotFoundError:
        raise


def write_json(new_dags_meta_data: dict, file_name: str):
    try:
        with open(f"{file_name}", 'w') as file:
            json.dump(new_dags_meta_data, file, indent=4, ensure_ascii=True, sort_keys=True)
        file.close()
    except FileNotFoundError:
        raise
