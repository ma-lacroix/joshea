from dataclasses import dataclass

from constants.run_status import RUN_STATUS


@dataclass
class TaskRunMetaData:
    name: str
    id: str
    status: RUN_STATUS
    total_run_time: int
