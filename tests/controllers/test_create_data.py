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

# def execute_create() -> json:
#     existing_dags = fetch_workflow_meta_data()
#     current_dags = parse_folder()
#     new_dags = list(set(current_dags) - set(existing_dags))
#     if len(new_dags) == 0:
#         return json.dumps({"Nothing new": ''})
#     dags_to_add = get_list_valid_dags(new_dags)
#     write_dag_meta_data_to_db(dags_to_add)
#     write_dag_names_run_data_to_db(dags_to_add)
#     return prepare_create_response([dag.turn_into_dict() for dag in dags_to_add])
