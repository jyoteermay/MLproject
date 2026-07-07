from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
        This function will return the list of requirement
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirements]
    

setup(
name='mlproject',
version='0.01',
author='Jyoteermaya',
packages=find_packages(),
install_requires=get_requirements("requirements.txt")
)