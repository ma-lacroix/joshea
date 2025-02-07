import unittest

from app.controllers.create_data import prepare_create_response


class TestCreateData(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_prepare_create_response_pass(self):
        dags = [{'name': 'one', 'tasks': ['t1', 't2']},
                {'name': 'two', 'tasks': ['t1', 't2']}]
        self.assertIsNotNone(prepare_create_response(dags))
