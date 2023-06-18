from setuptools import setup
from typing import List


PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Ashu"
DESCRIPTION = "This is a first FSDS Nov batch Machine Learning Project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(

    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = PACKAGES,
    install_requires = get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())