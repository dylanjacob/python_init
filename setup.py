import os
import sys
from setuptools import setup, find_packages
import versioneer

setup(
    name="project",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="",
    long_description="",
    url="",
    license="",
    classifiers=[],
    keywords=[],
    author="Dylan Jacob",
    author_email="dylan.jacob@bubblecore.net",
    packages=find_packages(),
    install_requires=[],
    scripts=[],
    entry_points={
        'console_scripts': [
            'project=project.manage',
        ]
    },
)
