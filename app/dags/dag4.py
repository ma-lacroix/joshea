# example DAG one
from time import sleep


def get_data():
    print("get_data()")
    sleep(5)

# _tasks_
# get_data()
