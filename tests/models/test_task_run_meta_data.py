import unittest

from app.constants.run_status import RUN_STATUS
from app.models.task_run_meta_data import TaskRunMetaData


class TestModelsTaskRunMetaData(unittest.TestCase):

    def setUp(self):
        self.dag = TaskRunMetaData("a", RUN_STATUS.RUNNING, 0)

    def test_turn_into_dict(self):
        self.assertEqual(RUN_STATUS.RUNNING, self.dag.turn_into_dict().get('status'))
        self.assertEqual(3, len(self.dag.turn_into_dict().keys()))
