# example DAG one

def get_data():
    pass


def get_more_data():
    pass


def get_a_lot_more_data():
    pass


def call_client():
    pass

# _tasks_
get_data() >> get_more_data() >> get_a_lot_more_data() >> call_client()
