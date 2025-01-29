from dataclasses import dataclass

from constants.run_status import RUN_STATUS


@dataclass
class TaskRunMetaData:
    date: str
    id: str
    status: RUN_STATUS
    total_run_time: int
