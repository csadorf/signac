# signac - simple data management

[![DOI](https://zenodo.org/badge/72946496.svg)](https://zenodo.org/badge/latestdoi/72946496)
[![PyPi](https://img.shields.io/pypi/v/signac.svg)](https://pypi.org/project/signac/)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/signac/badges/version.svg)](https://anaconda.org/conda-forge/signac)
[![conda-forge-downloads](https://img.shields.io/conda/dn/conda-forge/signac.svg)](https://anaconda.org/conda-forge/signac)
[![RTD](https://readthedocs.org/projects/signac/badge/?version=latest)](https://signac.readthedocs.io)
[![License](https://img.shields.io/github/license/csadorf/signac.svg)](https://bitbucket.org/glotzer/signac/src/master/LICENSE.txt)

## About

The [signac framework](http://www.signac.io) aids in the management of large and heterogeneous data spaces.

It provides a simple and robust data model to create a well-defined indexable storage layout for data and metadata.
This makes it easier to operate on large data spaces, streamlines post-processing and analysis and makes data collectively accessible.

**The package documentation is available at: [https://signac.readthedocs.io](https://signac.readthedocs.io)**

**The framework documentation is available at: [https://signac-docs.readthedocs.io](https://signac-docs.readthedocs.io)**

## Installation

The recommendend installation method for **signac** is through **conda** or **pip**.
The software is tested for python versions 2.7.x and 3.x and is built for all major platforms.

To install **signac** *via* the [conda-forge](https://conda-forge.github.io/) channel, execute:

    conda install -c conda-forge signac

To install **signac** *via* **pip**, execute:

    pip install signac

**Detailed information about alternative installation methods can be found in the [documentation](https://signac.readthedocs.io/en/latest/installation.html).**

## Quickstart

The framework facilitates a project-based workflow.
Setup a new project:

    $ mkdir my_project
    $ cd my_project
    $ signac init MyProject

and access the project handle:

    >>> project = signac.get_project()

## Documentation

The documentation for this package is hosted at [https://signac.readthedocs.io](https://signac.readthedocs.io).
We further invite you to check out the [framework documentation](https://signac-docs.readthedocs.io), which provides a more comprehensive overview over all components of the framework.

## Testing

You can test this package either by executing

    $ python -m unittest discover tests/

within the repository root directory or with [tox](https://tox.readthedocs.io/en/latest/).

## Acknowledgment

When using **signac** as part of your work towards a publication, we would really appreciate that you acknowledge **signac** appropriately.
We have prepared examples on how to do that [here](http://signac.readthedocs.io/en/latest/acknowledge.html).
**Thank you very much!**
