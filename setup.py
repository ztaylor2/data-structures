"""The setup for mailroom project in python."""
from setuptools import setup

setup(
    name="data-structures",
    description="Data structures written in python",
    version=0.1,
    author="Zach Taylor & John Jensen",
    author_email="zacharymtaylor3@gmail.com & jensen.john.r@gmail.com",
    license='MIT',
    py_modules=[],
    install_requires=['ipython'],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
    entry_points={
        'console_scripts': []
    }
)
