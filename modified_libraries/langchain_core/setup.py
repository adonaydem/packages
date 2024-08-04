from setuptools import setup, find_packages

setup(
    name='langchain_core',  # Name of your modified package
    version='0.2.28',  # Version of your modified package
    packages=find_packages(),  # Automatically find all packages and subpackages
    install_requires=[
        'jsonpatch>=1.33,<2.0',
        'jsonpointer>=1.9',
        'langsmith>=0.1.75,<0.2.0',
        'orjson>=3.9.14,<4.0.0',
        'pydantic>=1,<3',
        'annotated-types>=0.4.0',
        'pydantic_core==2.16.3',
        'typing_extensions>=4.6.0,!=4.7.0',
        'requests>=2,<3',
        'certifi>=2017.4.17',
        'charset-normalizer>=2,<4',
        'idna>=2.5,<4',
        'urllib3>=1.21.1,<3',
        'packaging>=23.2,<25',
        'PyYAML>=5.3',
        'tenacity>=8.1.0,<9.0.0,!=8.4.0'
    ],
)