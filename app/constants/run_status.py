class RUN_STATUS:
    # value colors are used by the HTML
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    PENDING = "pending"
    EMPTY = "empty"
    DELETED = "na_dag_deleted"
    colors = {
        "running": "blue",
        "success": "green",
        "failed": "red",
        "pending": "yellow",
        "empty": "light grey"
    }

