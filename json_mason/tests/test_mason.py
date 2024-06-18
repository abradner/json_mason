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


if __name__ == '__main__':
    unittest.main()
