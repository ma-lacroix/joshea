from dataclasses import dataclass


@dataclass
class DagRunMetaData:
    date: str
    id: str
    tasks: list
