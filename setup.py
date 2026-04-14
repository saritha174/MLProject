from setuptools import find_packages,setup
from typing import List

Hypen_dot_e = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
        this fucntion will retuen the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements]

        if Hypen_dot_e in requirements:
            requirements.remove(Hypen_dot_e)
    

        return requirements

setup(
    name = 'END_TO_END_ML_PROJECT',
    version= '0.0.1',
    author= 'Saritha',
    author_email= 'peddisaritha174@gmail.com',
    packages= find_packages(),
    install_requires=get_requirements('requirements.txt')


)