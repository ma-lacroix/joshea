import unittest
from unittest.mock import patch

from app.main import app


class TestGetNextDagRun(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    @patch("app.main.read_data.fetch_next_run", return_value={"status": "all good"})
    def test_get_next_dag_run(self, mock_fetch_next_run):
        response = self.app.get("/r/get_next_dag_run?name=my_dag")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "all good"})

    @patch("app.main.create_data.execute_create", return_value={"status": "all good"})
    def test_find_new_workflows(self, mock_schedule):
        response = self.app.post("/c/submit_new")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "all good"})

    @patch("app.main.create_data.schedule_dag_run", return_value={"status": "all good"})
    def test_start_new_dag_run(self, mock_schedule):
        response = self.app.post("/c/schedule_dag_run", json={"test": True})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "all good"})

    @patch("app.main.update_data.execute_dag", return_value={"status": "all good"})
    def test_run_dag(self, mock_schedule):
        response = self.app.post("/u/execute_dag", json={"test": True})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "all good"})

    @patch("app.main.delete_data.flush_meta_data", return_value={"status": "all good"})
    def test_reset_meta_data(self, mock_schedule):
        response = self.app.post("/d/remove_all", json={"test": True})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "all good"})

    @patch("app.main.delete_data.delete_workflow", return_value={"status": "all good"})
    def test_delete_dag(self, mock_schedule):
        response = self.app.post("/d/remove_dag", json={"test": True})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "all good"})