from setuptools import find_packages,setup
from typing import List

requirement_file_name = "requirements.txt"
REMOVE_PACKAGE = "-e ."
def get_requirements()->List[str]: # return list of requirements in string
    with open(requirement_file_name) as rf:
        requriment_list = rf.readline()
        requriment_list = [requriment_name.replace("\n", "") for requriment_name in requriment_list]

        if REMOVE_PACKAGE in requriment_list:
            requriment_list.remove(REMOVE_PACKAGE)
        return requriment_list







setup(
    name='Insurance',
    version='0.0.1',
    description='Industry level project',
    author='Anurag Singh',
    author_email='anurag.anurag.singh864@gmail.com',
    packages= find_packages(), #find where the init file
    install_reqires = get_requirements()
)
