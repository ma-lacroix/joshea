from dataclasses import dataclass


@dataclass
class DagRunsMetaData:
    name: str
    runs: list
