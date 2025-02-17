import unittest

from app.constants.run_status import RUN_STATUS


class TestRunStatus(unittest.TestCase):

    def setUp(self) -> None:
        self.run_status = RUN_STATUS

    def test_all_values(self):
        self.assertEqual(RUN_STATUS.RUNNING, self.run_status.RUNNING)
        self.assertEqual(RUN_STATUS.PENDING, self.run_status.PENDING)
        self.assertEqual(RUN_STATUS.EMPTY, self.run_status.EMPTY)
        self.assertEqual(RUN_STATUS.FAILED, self.run_status.FAILED)
        self.assertEqual(RUN_STATUS.SUCCESS, self.run_status.SUCCESS)
        self.assertEqual("blue", self.run_status.colors.get(RUN_STATUS.RUNNING))
        self.assertEqual("green", self.run_status.colors.get(RUN_STATUS.SUCCESS))
        self.assertEqual("red", self.run_status.colors.get(RUN_STATUS.FAILED))
        self.assertEqual("yellow", self.run_status.colors.get(RUN_STATUS.PENDING))
        self.assertEqual("light grey", self.run_status.colors.get(RUN_STATUS.EMPTY))
