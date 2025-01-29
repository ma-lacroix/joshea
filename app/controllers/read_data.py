from utils.general_utils import get_json
from constants import values


def fetch_meta_data():
    return get_json(values.META_DATA)
