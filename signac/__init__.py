# Copyright (c) 2017 The Regents of the University of Michigan
# All rights reserved.
# This software is licensed under the BSD 3-Clause License.
"""The signac framework aids in the management of large and
heterogeneous data spaces.

It provides a simple and robust data model to create a
well-defined indexable storage layout for data and metadata.
This makes it easier to operate on large data spaces,
streamlines post-processing and analysis and makes data
collectively accessible."""

from __future__ import absolute_import
from . import contrib
from . import db
from . import cite
from . import errors
from . import sync
from .contrib import Project
from .contrib import get_project
from .contrib import init_project
from .contrib import fetch
from .contrib import export_one
from .contrib import export
from .contrib import export_to_mirror
from .contrib import export_pymongo
from .contrib import fetch_one  # deprecated
from .contrib import filesystems as fs
from .contrib import Collection
from .contrib import index_files
from .contrib import index
from .contrib import RegexFileCrawler
from .contrib import MasterCrawler
from .contrib import SignacProjectCrawler
from .db import get_database
from .core.jsondict import buffer_reads_writes as buffered
from .core.jsondict import in_buffered_mode as is_buffered
from .core.jsondict import flush_all as flush
from .core.jsondict import get_buffer_size
from .core.jsondict import get_buffer_load


__version__ = '0.9.3'

__all__ = ['__version__', 'contrib', 'db', 'errors', 'sync',
           'cite',
           'Project', 'get_project', 'init_project',
           'get_database', 'fetch', 'fetch_one',
           'export_one', 'export', 'export_to_mirror',
           'Collection',
           'export_pymongo', 'fs',
           'index_files', 'index',
           'RegexFileCrawler',
           'MasterCrawler',
           'SignacProjectCrawler',
           'buffered', 'is_buffered', 'flush', 'get_buffer_size', 'get_buffer_load',
           ]
