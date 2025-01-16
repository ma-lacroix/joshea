# example DAG one

def get_data():
    pass


def process_data():
    pass


def write_to_db():
    pass


# _tasks_
get_data() >> process_data() >> write_to_db()
