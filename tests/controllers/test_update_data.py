import unittest
from unittest.mock import patch

from app.constants.run_status import RUN_STATUS
from app.controllers import update_data


class TestUpdateData(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @patch('app.controllers.update_data.get_json', return_value={"dag1.py": {"2025-02-11 10:35:11": {}}})
    def test_validate_dag_execution_request_pass(self, mock_get_json):
        self.assertEqual(True, update_data.validate_dag_execution_request("dag1.py", "2025-02-11 10:35:11"))

    @patch('app.controllers.update_data.get_json', return_value={"dag1.py": {"2025-02-11 10:35:11": {}}})
    def test_validate_dag_execution_request_fail(self, mock_get_json):
        self.assertEqual(False, update_data.validate_dag_execution_request("dag2.py", "2025-02-11 10:35:11"))

    @patch('app.controllers.update_data.get_json', return_value={"workflows":
                                                                     {"dd1.py":
                                                                          ["get_data", "process_data", "write_to_db"]}})
    def test_fetch_workflow_task_names_pass(self, mock_get_json):
        self.assertEqual(3, len(update_data.fetch_workflow_task_names("dd1.py")))

    @patch('app.controllers.update_data.get_json', return_value={
            "dag1.py": {
                "2025-02-08 21:01:01": {
                    "status": "success",
                    "tasks": {
                        "get_data": {
                            "id": "d88e6d3f-4628-4caa-b57d-81e8cc0baeac",
                            "status": "pending",
                            "total_run_time": 0
                        }}}}})
    @patch('app.controllers.update_data.write_json', return_value=None)
    def test_update_dag_task_run_status_pass(self, mock_get_json, mock_write_json):
        self.assertEqual(True, update_data.update_dag_task_run_status(dag_name='dag1.py',
                                                                      id='2025-02-08 21:01:01',
                                                                      task_name='get_data',
                                                                      new_status=RUN_STATUS.RUNNING))

    @patch('app.controllers.update_data.validate_dag_execution_request', return_value=False)
    def test_execute_dag_validation_fail(self, mock_validate_dag_execution_request):
        self.assertEqual({'status': RUN_STATUS.FAILED, 'message': 'Run ID does not exist'},
                         update_data.execute_dag("test", "test"))

    @patch('app.controllers.update_data.fetch_workflow_task_names', return_value={"workflows": {"dd1.py": ["get_data", "process_data", "write_to_db"]}})
    @patch('app.controllers.update_data.validate_dag_execution_request', return_value=True)
    @patch('app.controllers.update_data.update_dag_task_run_status', return_value=True)
    @patch('app.controllers.update_data.execute_dag_task', return_value=None)
    def test_execute_dag_pass(self, mock_task_names, mock_validate_req, mock_run_status, mock_task_execution):
        self.assertEqual(RUN_STATUS.SUCCESS, update_data.execute_dag("test", "id").get('status'))

    @patch('app.controllers.update_data.fetch_workflow_task_names', return_value={"workflows": {"dd1.py": ["get_data", "process_data", "write_to_db"]}})
    @patch('app.controllers.update_data.validate_dag_execution_request', return_value=True)
    @patch('app.controllers.update_data.update_dag_task_run_status', return_value=True)
    @patch('app.controllers.update_data.execute_dag_task', side_effect=Exception("Task execution failed"))
    @patch("time.sleep", return_value=None)
    def test_execute_dag_pass(self, mock_task_names, mock_validate_req, mock_run_status, mock_task_execution, mock_sleep):
        self.assertEqual(RUN_STATUS.FAILED, update_data.execute_dag("test", "id").get('status'))
