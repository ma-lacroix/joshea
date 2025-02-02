from dataclasses import dataclass

from constants.run_status import RUN_STATUS


@dataclass
class DagRunMetaData:
    status: RUN_STATUS
    tasks: dict

    def turn_into_dict(self):
        return {
            "status": self.status,
            "tasks": self.handle_tasks()
        }

    def handle_tasks(self):
        tasks_dict = {}
        for key in self.tasks:
            tasks_dict[key] = self.tasks[key].turn_into_dict()
        return tasks_dict
