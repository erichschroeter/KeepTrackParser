#!/usr/bin/env python
"""KeepTrack parses exported CSV files from the KeepTrack app.

Usage:
  KeepTrack.py (-v | --version)
  KeepTrack.py (-h | --help)

Options:
  -h --help                Show this screen and exit.
  -v --version             Show the version and exit.

"""

from docopt import docopt

def main():
    arguments = docopt( __doc__, version='KeepTrack v1.0')
    print( arguments )

if __name__ == '__main__':
    main()
