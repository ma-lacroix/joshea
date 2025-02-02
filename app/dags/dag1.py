# example DAG one
from time import sleep


def get_data():
    print("get_data()")
    sleep(5)


def process_data():
    print("process_data()")
    sleep(5)


def write_to_db():
    print("write_to_db()")
    sleep(5)


# _tasks_
# get_data() >> process_data() >> write_to_db()
