import unittest
from unittest.mock import patch

from app.controllers import delete_data


class TestDeleteData(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @patch('app.controllers.delete_data.write_json', return_value=None)
    def test_flush_meta_data(self, mock_write_json):
        self.assertEqual("Meta data reset", delete_data.flush_meta_data())
