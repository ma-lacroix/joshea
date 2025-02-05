import unittest

from app.constants.run_status import RUN_STATUS
from app.models.run_meta_data import DagRunMetaData
from app.models.task_run_meta_data import TaskRunMetaData


class TestModels(unittest.TestCase):

    def setUp(self):
        self.dag = DagRunMetaData(RUN_STATUS.PENDING, {'task1': TaskRunMetaData("a", RUN_STATUS.RUNNING, 0)})

    def test_turn_into_dict(self):
        self.assertEqual(RUN_STATUS.PENDING, self.dag.turn_into_dict().get('status'))
        self.assertEqual(2, len(self.dag.turn_into_dict().keys()))
