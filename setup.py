from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_form_rai/__init__.py
from frappe_form_rai import __version__ as version

setup(
	name="frappe_form_rai",
	version=version,
	description="Forms for GNE Students Interaction",
	author="H S Rai",
	author_email="hardeep.rai@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
