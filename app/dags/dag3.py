# example DAG one
from time import sleep


def get_data():
    print("get_data()")
    sleep(5)


def get_more_data():
    print("get_more_data()")
    sleep(5)


def get_a_lot_more_data():
    print("get_a_lot_more_data()")
    sleep(5)


def call_client():
    print("get_call_client()")
    sleep(5)

# _tasks_
# get_data() >> get_more_data() >> get_a_lot_more_data() >> call_client()
