
class DagMetaData:

    def __init__(self, name: str, tasks: list):
        self.name = name
        self.tasks = tasks

    def turn_into_dict(self):
        return {'name': self.name, 'tasks': self.tasks}
