import json
from typing import List, Union, IO


class BuildingBlocks:
    def __init__(self):
        self.blocks = {}
        self.hash_map = {}


class JSONBundle:
    def __init__(self, source_data: List[Union[str, bytes, IO[str]]]):
        self.data = [self.load_json(element) for element in source_data]

    @staticmethod
    def load_json(element: Union[str, bytes, IO[str]]) -> dict:
        if isinstance(element, str):
            return json.loads(element)
        elif isinstance(element, bytes):
            return json.loads(element.decode('utf-8'))
        else:
            return json.loads(element.read())

    @classmethod
    def from_preprocessed(cls, preprocessed_data: List[dict]):
        instance = cls.__new__(cls)
        instance.data = preprocessed_data
        return instance
