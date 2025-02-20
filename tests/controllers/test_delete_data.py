import unittest
from unittest.mock import patch

from app.controllers import delete_data


class TestDeleteData(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @patch('app.controllers.delete_data.write_json', return_value=None)
    def test_flush_meta_data_pass(self, mock_write_json):
        self.assertEqual("Meta data reset", delete_data.flush_meta_data())

    @patch('app.controllers.delete_data.write_json', side_effect=FileNotFoundError)
    def test_flush_meta_data_fail(self, mock_write_json):
        self.assertEqual("Failed to delete data!", delete_data.flush_meta_data())

    @patch('app.controllers.delete_data.write_json', return_value=None)
    @patch('app.controllers.delete_data.get_json', return_value={"workflows": {"dag1.py": ['get_data']}})
    def test_delete_workflow_pass(self, mock_write_json, mock_get_json):
        self.assertEqual("Deleted dag1.py successfully", delete_data.delete_workflow('dag1.py'))

    @patch('app.controllers.delete_data.get_json', side_effect=FileNotFoundError)
    def test_delete_workflow_fail(self, mock_write_json):
        self.assertEqual("Failed to delete dag1.py", delete_data.delete_workflow('dag1.py'))