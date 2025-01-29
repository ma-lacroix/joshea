from dataclasses import dataclass

from constants.run_status import RUN_STATUS


@dataclass
class DagRunMetaData:
    date: str
    status: RUN_STATUS
    tasks: list

    def turn_into_dict(self):
        return {
            "date": self.date,
            "status": self.status,
            "tasks": [{
                "name": task.name,
                "id": task.id,
                "status": task.status,
                "total_run_time": task.total_run_time} for task in self.tasks]
        }
