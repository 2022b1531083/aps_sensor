from setuptools import setup,find_packages
from typing import List

def get_requirements() -> List[str]:
    requirements_list: List[str] = []
    with open("requirements.txt") as file:
        requirements_list = file.readlines()
        requirements_list = [req.strip() for req in requirements_list if req.strip() and not req.startswith("-e")]
    return requirements_list

setup (
    name='Sensor',
    version="0.0.1",
    author="Yogesh",
    author_email="yogiafse@gmail.com",
    packages=['Sensor'],
    install_requires=  get_requirements()           #["pymongo"]
)