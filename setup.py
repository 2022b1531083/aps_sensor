from setuptools import setup,find_packages

def get_requirements()->list[str]:
    
    requirements_list =list[str]=[]
    
    return requirements_list

setup (
    name='Sensor',
    version="0.0.1",
    author="Yogesh",
    author_email="yogiafse@gmail.com",
    packages=['Sensor'],
    install_requires=  get_requirements()           #["pymongo"]
)