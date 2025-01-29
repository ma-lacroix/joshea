from dataclasses import dataclass


@dataclass
class DagMetaData:
    name: str
    tasks: list

    def turn_into_dict(self):
        return {'name': self.name, 'tasks': self.tasks}
