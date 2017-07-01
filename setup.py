from __future__ import print_function
import sys
import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install

if sys.version_info < (2, 7, 0):
    print("Error: signac requires python version >= 2.7.x.")
    sys.exit(1)


class CheckExecutableCommand(install):
    def run(self):
        super(CheckExecutableCommand, self).run()
        try:
            subprocess.check_output('signac')
        except OSError as e:
            print("COULD NOT START SIGNAC!!", e)


setup(
    name='signac',
    version='0.8.5',
    packages=find_packages(),
    zip_safe=True,

    author='Carl Simon Adorf',
    author_email='csadorf@umich.edu',
    description="Simple data management framework.",
    keywords='simulation database index collaboration workflow',
    url="https://bitbucket.org/glotzer/signac",

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Topic :: Scientific/Engineering :: Physics",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],

    extras_require={
        'db': ['pymongo>=3.0'],
        'mpi': ['mpi4py'],
    },

    entry_points={
        'console_scripts': [
            'signac = signac.__main__:main',
        ],
    },

    cmdclass={
        'install': CheckExecutableCommand,
    },
)
