from app.constants import values
from app.constants.run_status import RUN_STATUS
from app.utils.general_utils import write_json, get_json


def flush_meta_data() -> str:
    """
    Resets all the DAG metadata
    """
    msg = "Meta data reset"
    try:
        write_json({'workflows': {}}, values.META_DATA)
        write_json({}, values.RUNS_DATA)
    except FileNotFoundError as e:
        msg = "Failed to delete data!"
    return msg


def delete_workflow(dag_name: str) -> str:
    """
    Flags a DAG's metadata as 'deleted'
    """
    msg = f"Deleted {dag_name} successfully"
    try:
        meta_data = get_json(values.META_DATA)
        meta_data["workflows"][dag_name] = RUN_STATUS.DELETED
        write_json(meta_data, values.META_DATA)
    except FileNotFoundError as e:
        msg = f"Failed to delete {dag_name}"
    return msg

