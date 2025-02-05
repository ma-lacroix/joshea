import unittest

from app.models.dag_meta_data import DagMetaData


class TestModels(unittest.TestCase):

    def setUp(self):
        self.dag = DagMetaData("test_name", ['task1', 'task2'])

    def test_turn_into_dict(self):
        self.assertEqual('test_name', self.dag.turn_into_dict().get('name'))
        self.assertEqual(2, len(self.dag.turn_into_dict().get('tasks')))
