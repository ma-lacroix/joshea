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


def get_meta_data() -> dict:
    try:
        with open(f"{values.META_DATA}", 'r') as file:
            meta_data = json.load(file)
        file.close()
        return meta_data
    except FileNotFoundError:
        raise


def write_meta_data(new_dags_meta_data: dict):
    try:
        with open(f"{values.META_DATA}", 'w') as file:
            json.dump(new_dags_meta_data, file, indent=4, ensure_ascii=True)
        file.close()
    except FileNotFoundError:
        raise


