from utils.general_utils import write_json
from constants import values


def flush_meta_data() -> str:
    write_json({'workflows': {}}, values.META_DATA)
    write_json({}, values.RUNS_DATA)
    return "Meta data reset"
