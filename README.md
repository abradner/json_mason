# JSON Mason - a content-aware JSON Compression Tool

## Overview

This project aims to intelligently compress a collection of JSON-serializable dictionaries by identifying and leveraging similarities among high-level objects and string values. The similarities - or "building blocks" - represent frequent patterns or object structures within the data, allowing for efficient representation and storage.

## Workflow

1. **Building Blocks Identification (`build_blocks`)**:
    - Parses input JSON data to identify reusable structures called "building blocks."
    - These blocks are used to compose more complex JSON objects in a more space-efficient manner.

2. **Compression (`compress`)**:
    - Replaces parts of JSON objects with references to predefined building blocks, effectively compressing the original JSON data into a template that uses less space.

3. **Decompression (`decompress`)**:
    - Reconstructs the original JSON data from the compressed templates using the building blocks, ensuring data integrity and reversibility.

## Usage

- **Building Blocks Creation**:
    - Input: List of JSON strings or JSON-compatible streams.
    - Output: A `BuildingBlocks` object representing identified reusable components.

- **Compression**:
    - Input: Original JSON data and `BuildingBlocks`.
    - Output: List of compressed JSON templates.

- **Decompression**:
    - Input: Compressed JSON templates and `BuildingBlocks`.
    - Output: List of decompressed, JSON-serializable dictionaries.

This approach is particularly useful for datasets with redundant data structures or for applications where storage efficiency is crucial.


## Example

```python
from json_mason import JSONMason

# Sample JSON data
source_data = [
    '{"a": 1, "b": 2, "c": 3}',
    '{"c": 50, "d": 60, "e": 70}',
    '{"b": 10, "d": 100}'
]

# Build building blocks
blocks = JSONMason.build_blocks(source_data)

# Compress JSON data
compressed_data = JSONMason.compress(source_data, blocks)

# Decompress JSON data
decompressed_data = JSONMason.decompress(compressed_data, blocks)

print(decompressed_data)
```
