import re

from app.models.dag_meta_data import DagMetaData


def validate_dag(dag: str) -> bool:
    """
    Validates the Python files used to run DAGs
    """
    return bool(re.match(r'^.*\.py$', dag.lower().strip()))


def parse_dag_file(dag: str) -> DagMetaData:
    """
    Reads the Python code and creates metadata
    """
    tasks = []
    with open(f"app/dags/{dag}", 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if line.strip() == "# _tasks_":
                tasks = re.sub(r'\([^)]*\)', '', lines[i + 1].strip().replace('#', '')).split(">>")
    return DagMetaData(dag, [task.replace(' ', '') for task in tasks])
