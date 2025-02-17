import unittest
from unittest.mock import patch, mock_open

from app.controllers import validator


class TestValidator(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_validate_dag_pass(self):
        self.assertEqual(True, validator.validate_dag("dag.py"))

    def test_validate_dag_false(self):
        self.assertEqual(False, validator.validate_dag("dag.csv"))

    @patch('app.controllers.validator.open', new_callable=mock_open, read_data="""
    # example DAG one
    from time import sleep
    def get_data():
        print("get_data()")
    def process_data():
        print("process_data()")
    def write_to_db():
        print("write_to_db()")
    # _tasks_
    # get_data() >> process_data() >> write_to_db()
    """)
    def test_parse_dag_file_pass(self, mocked_open):
        self.assertEqual("some_dag", validator.parse_dag_file("some_dag").name)
