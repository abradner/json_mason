import io
import json
import unittest

from json_mason.models import JSONBundle


class TestJSONBundle(unittest.TestCase):
    def setUp(self):
        self.preprocessed_data = [
            {
                "int": 1,
                "float": 1.1,
                "string": "test",
                "bool": True,
                "array": [1, 1.1, "test", True],
                "object": {
                    "int": 2,
                    "float": 2.2,
                    "string": "test2",
                    "bool": False
                }
            },
            {
                "int": 3,
                "float": 3.3,
                "string": "test3",
                "bool": True,
                "array": [3, 3.3, "test3", True],
                "object": {
                    "int": 4,
                    "float": 4.4,
                    "string": "test4",
                    "bool": False
                }
            }
        ]
        self.str_data = [json.dumps(data) for data in self.preprocessed_data]
        self.bytes_data = [data.encode('utf-8') for data in self.str_data]
        self.file_like_data = [io.StringIO(data) for data in self.str_data]

    def test_init_with_str_data(self):
        bundle = JSONBundle(self.str_data)
        self.assertEqual(bundle.data, self.preprocessed_data)

    def test_init_with_bytes_data(self):
        bundle = JSONBundle(self.bytes_data)
        self.assertEqual(bundle.data, self.preprocessed_data)

    def test_init_with_file_like_data(self):
        bundle = JSONBundle(self.file_like_data)
        self.assertEqual(bundle.data, self.preprocessed_data)

    def test_init_with_mixed_data(self):
        bundle = JSONBundle(self.str_data + self.bytes_data + self.file_like_data)
        self.assertEqual(bundle.data, self.preprocessed_data * 3)

    def test_from_preprocessed(self):
        bundle = JSONBundle.from_preprocessed(self.preprocessed_data)
        self.assertEqual(bundle.data, self.preprocessed_data)

if __name__ == '__main__':
    unittest.main()
