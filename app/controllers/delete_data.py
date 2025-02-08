from app.constants import values
from app.utils.general_utils import write_json


def flush_meta_data() -> str:
    msg = "Meta data reset"
    try:
        write_json({'workflows': {}}, values.META_DATA)
        write_json({}, values.RUNS_DATA)
    except FileNotFoundError as e:
        msg = "Failed to delete data!"
    return msg

