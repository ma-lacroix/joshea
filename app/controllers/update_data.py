from utils.general_utils import write_meta_data


def flush_meta_data() -> str:
    write_meta_data({'workflows': {}})
    return "Meta data reset"
