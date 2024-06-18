# test_json_compressor.py

import unittest

from ..mason import JSONMason, BuildingBlocks


class TestJSONMason(unittest.TestCase):
    def setUp(self):
        self.source_data = [
            '{"a": 1, "b": 2, "c": 3}',
            '{"c": 50, "d": 60, "e": 70}',
            '{"b": 10, "d": 100}'
        ]
        self.blocks = JSONMason.build_blocks(self.source_data)

    def test_build_blocks(self):
        blocks = JSONMason.build_blocks(self.source_data)
        self.assertIsInstance(blocks, BuildingBlocks)
        # Add more assertions to verify the content of blocks

    def test_compress(self):
        compressed_data = JSONMason.compress(self.source_data, self.blocks)
        self.assertIsInstance(compressed_data, list)
        # Add more assertions to verify the content of compressed_data

    def test_decompress(self):
        compressed_data = JSONMason.compress(self.source_data, self.blocks)
        decompressed_data = JSONMason.decompress(compressed_data, self.blocks)
        self.assertIsInstance(decompressed_data, list)
        # Add more assertions to verify the content of decompressed_data

def test_parse_json():
    json_input = '{"name": "JSONMason", "active": true}'
    expected_output = {"name": "JSONMason", "active": True}
    assert parse_json(json_input) == expected_output

def test_find_common_structures():
    data = [
        {"name": "JSONMason", "active": True},
        {"name": "JSONMason", "active": False}
    ]
    # Assuming find_common_structures returns a list of common keys
    assert 'name' in find_common_structures(data)
    assert 'active' in find_common_structures(data)

def test_build_blocks_integration():
    source_data = ['{"name": "JSONMason", "active": true}', '{"name": "JSONMason", "active": false}']
    blocks = JSONMason.build_blocks(source_data)
    # Test if blocks contain the correct structures
    assert 'name' in blocks.keys()


if __name__ == '__main__':
    unittest.main()
