# example DAG one

def get_data():
    print("get_data()")


def process_data():
    print("process_data()")


def write_to_db():
    print("write_to_db()")


# _tasks_
# get_data() >> process_data() >> write_to_db()
