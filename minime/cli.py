# -*- coding: utf-8 -*-

"""
Main CLI entry point
"""

from docopt import docopt

from . import __doc__, __title__, __version__


def main():
    version = '%s %s' % (__title__, __version__)
    args = docopt(__doc__, version=version)
