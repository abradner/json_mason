from setuptools import setup, find_packages

setup(
    name='json_mason',
    version='0.1.0',
    packages=find_packages(),
    description='A smart JSON compressor tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Alex Bradner',
    author_email='me@alexbradner.com',
    url='https://github.com/abradner/json_mason',
    install_requires=[
    ],
    tests_require=[
        'pytest',
    ],
    python_requires='>=3.10',
)
