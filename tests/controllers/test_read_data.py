import unittest

from app.controllers import read_data


class TestReadData(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_get_task_statuses_pass(self) -> None:
        data = [{"status": "success", "tasks": {"get_data": {"status": "success"}}},
                {"status": "pending", "tasks": {"get_data": {"status": "pending"}}}]
        self.assertEqual(['green', 'yellow'], read_data.get_task_statuses(data, 'get_data')[0:2])

    def test_sort_runs_by_scheduled_date_pass(self):
        data = {11: "eleven", 4: "four", 3: "three", 5: "five"}
        self.assertEqual("eleven", read_data.sort_runs_by_scheduled_date(data)[3])

    def test_merge_data(self):
        meta_data = {"dag1.py": ["get_data"],
                     "dag2.py": ["get_data", "get_more_data"]}
        runs_data = {
            "dag1.py": {
                "2025-02-08 21:01:01": {
                    "status": "success",
                    "tasks": {
                        "get_data": {
                            "id": "d88e6d3f-4628-4caa-b57d-81e8cc0baeac",
                            "status": "success",
                            "total_run_time": 0},
                    }
                },
                "2025-02-08 21:01:04": {
                    "status": "pending",
                    "tasks": {
                        "get_data": {
                            "id": "4f954481-b890-4204-a368-e64244b54eca",
                            "status": "pending",
                            "total_run_time": 0
                        }
                    }
                }
            },
            "dag2.py": {
                "2025-02-08 21:01:07": {
                    "status": "failed",
                    "tasks": {
                        "get_data": {
                            "id": "d123c735-8ade-4840-a393-7349fb3f687f",
                            "status": "failed",
                            "total_run_time": 0
                        },
                        "get_more_data": {
                            "id": "7444fb0b-b590-4526-8eee-7e2c8c8d28e9",
                            "status": "pending",
                            "total_run_time": 0
                        }
                    }
                }
            }
        }
        print(read_data.merge_data(meta_data, runs_data))
