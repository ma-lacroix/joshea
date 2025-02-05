from dataclasses import dataclass

from app.constants.run_status import RUN_STATUS


@dataclass
class TaskRunMetaData:
    id: str
    status: RUN_STATUS
    total_run_time: int

    def turn_into_dict(self):
        return {"id": self.id, "status": self.status, "total_run_time": self.total_run_time}
