""" __Doc__ File handle class """
from setuptools import find_packages, setup
from scripts.AutoGPenT0ols.lib.core.__version__ import __version__


def dependencies(imported_file):
    """ __Doc__ Handles dependencies """
    with open(imported_file) as file:
        return file.read().splitlines()


with open("README.md") as file:
    setup(
        name="GPT0ols",
        license="GPLv3",
        description="Final PRoject "
        " ",
        long_description=file.read(),
        author="Capitan J4ck",
        version=__version__,
        author_email="internetghost2@protonmail.com",
        url="https://github.com/Th3FirstAvenger/GPenT0ols",
#        packages=find_packages(
#        package_data={
#            'scripts/AutoGPenT0ols/': [
#                '*.txt',
#                '*.json']},
#        entry_points={
#            'console_scripts': ['GPT0ols = AutoGPenT0ols.GPenT0ols:main']},
#        include_package_data=True)
