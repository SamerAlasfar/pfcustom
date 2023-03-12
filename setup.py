from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pfcustom/__init__.py
from pfcustom import __version__ as version

setup(
	name="pfcustom",
	version=version,
	description="all erp customization for pf",
	author="Asdamsoft",
	author_email="info@asdamsoft.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
