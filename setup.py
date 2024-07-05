from setuptools import setup, find_packages

setup(
	name='mypackage',
	version='0.1',
	packages=find_packages(exclude=['tests*']),
	license='MIT',
	description='EDSA example python package',
	long_descriptions=open('README.md').read(),
	install_requires=['numpy'],
	url='https://github.com/Robert-Breedt/sustainable-forest-management.git',
	author='Robert Breedt',
	author_email='breedtrobert@yahoo.com'
)