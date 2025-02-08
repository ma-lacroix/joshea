import unittest

from app.controllers import read_data


class TestReadData(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_get_task_statuses(self) -> None:
        data = [{"status": "success", "tasks": {"get_data": {"status": "success"}}},
                {"status": "pending", "tasks": {"get_data": {"status": "pending"}}}]
        self.assertEqual(['green', 'yellow'], read_data.get_task_statuses(data, 'get_data')[0:2])
