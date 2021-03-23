import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
	name='PyYep',
	version='0.0.1',
	author='Daniel Montalvão Bomfim',
	author_email='daniellsmv@hotmail.com',
	description='A simple schema builder for value parsing and validation',
	long_description=long_description,
	packages=['PyYep'],
	python_requires='>=3.6',
	url='https://github.com/Daniel775/PyYep',
    project_urls={
        'Bug Tracker': 'https://github.com/Daniel775/PyYep/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
