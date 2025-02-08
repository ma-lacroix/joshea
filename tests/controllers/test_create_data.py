import unittest
from unittest.mock import patch

from app.controllers import create_data
from app.controllers.create_data import prepare_create_response
from app.models.dag_meta_data import DagMetaData


class TestCreateData(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_prepare_create_response_pass(self):
        dags = [{'name': 'one', 'tasks': ['t1', 't2']},
                {'name': 'two', 'tasks': ['t1', 't2']}]
        self.assertIsNotNone(prepare_create_response(dags))

    @patch('app.controllers.create_data.validate_dag', return_value=True)
    @patch('app.controllers.create_data.parse_dag_file', return_value=DagMetaData('dag', ['task1', 'task2']))
    def test_get_list_valid_dags_pass(self, mock_parse_dag_file, mock_validate_dag):
        new_dags = ['da.py']
        self.assertEqual(1, len(create_data.get_list_valid_dags(new_dags)))

    @patch('app.controllers.create_data.validate_dag', return_value=False)
    @patch('app.controllers.create_data.parse_dag_file', return_value=DagMetaData('dag', ['task1', 'task2']))
    def test_get_list_valid_dags_fail(self, mock_parse_dag_file, mock_validate_dag):
        new_dags = ['da.py']
        self.assertEqual(0, len(create_data.get_list_valid_dags(new_dags)))

    @patch('app.controllers.create_data.fetch_workflow_meta_data', return_value=['dd1', 'dd2'])
    @patch('app.controllers.create_data.parse_folder', return_value=['dd3', 'dd4'])
    @patch('app.controllers.create_data.write_dag_meta_data_to_db', return_value=None)
    @patch('app.controllers.create_data.write_dag_names_run_data_to_db', return_value=None)
    @patch('app.controllers.create_data.validate_dag', return_value=False)
    @patch('app.controllers.create_data.parse_dag_file', return_value=DagMetaData('dag', ['task1', 'task2']))
    def test_execute_create_pass(self, mock_fetch_workflow_meta_data, mock_parse_folder,
                                 mock_write_dag_meta_data_to_db, mock_write_dag_names_run_data_to_db,
                                 mock_parse_dag_file, mock_validate_dag):
        self.assertEqual(0, len(create_data.execute_create()))

    @patch('app.controllers.create_data.fetch_workflow_meta_data', return_value=['dd1', 'dd2'])
    @patch('app.controllers.create_data.parse_folder', return_value=['dd1', 'dd2'])
    def test_execute_create_fail(self, mock_fetch_workflow_meta_data, mock_parse_folder):
        self.assertEqual("nothing new", create_data.execute_create().get("message"))

    @patch('app.controllers.create_data.fetch_workflow_meta_data', return_value=['dd1.py', 'dd2.py'])
    @patch('app.controllers.create_data.get_json', return_value={"workflows":
                                                                     {"dd1.py":
                                                                          ["get_data", "process_data", "write_to_db"]}})
    @patch('app.controllers.create_data.add_new_dag_run_to_db', return_value=None)
    def test_schedule_dag_run_pass(self, mock_fetch_workflow_meta_data, mock_get_json, mock_add_new_dag_run_to_db):
        data = create_data.schedule_dag_run({"name": 'dd1.py'})
        self.assertEqual("pending", data.status)

    @patch('app.controllers.create_data.fetch_workflow_meta_data', return_value=['dd1.py', 'dd2.py'])
    def test_schedule_dag_run_fail(self, mock_fetch_workflow_meta_data):
        data = create_data.schedule_dag_run({"name": 'bad_key'})
        self.assertEqual({'Invalid POST request, missing key bad_key'}, data)