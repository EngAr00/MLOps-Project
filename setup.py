from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirement(file_path:str)->List[str]:
    '''This function will return the list of requirement'''
    requirements= []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


setup (
    name='mlproject',
    version='0.0.1',
    author='Abdrizack',
    author_email='abdirizackhussein1112769@gmail.com',
    packages=find_packages(),
    install_requires = get_requirement('requirements.txt')
    )