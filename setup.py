from setuptools import setup
from typing import List


# declaring variables for setup functions

PROJECT_NAME = "housing_predictor"
VERSION = "0.0.1"
AUTHOR = "Owais Nawaz"
DESCRIPTION = "This is a ML Project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list() -> List[str]:
    """This function will return a list of requirements mentioned in requirements.txt"""
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list(),
)
