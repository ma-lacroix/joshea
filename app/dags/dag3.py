# example DAG one

def get_data():
    print("get_data()")


def get_more_data():
    print("get_more_data()")


def get_a_lot_more_data():
    print("get_a_lot_more_data()")


def call_client():
    print("get_call_client()")

# _tasks_
# get_data() >> get_more_data() >> get_a_lot_more_data() >> call_client()
