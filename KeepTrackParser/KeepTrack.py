#!/usr/bin/env python
"""KeepTrack parses exported CSV files from the KeepTrack app.

Usage:
  KeepTrack.py trackers [--include-lineno] <keeptrack-csv-file>
  KeepTrack.py (-v | --version)
  KeepTrack.py (-h | --help)

Options:
  -h --help                Show this screen and exit.
  -v --version             Show the version and exit.

"""

from docopt import docopt
import csv

class KeepTrack_CSV_Entry( object ):
    def __init__( self, lineno, csv_string ):
        self.lineno = lineno
        self.csv_string = csv_string

def list_keeptrack_trackers( csv_file_path, tracker_found_callback=None ):
    trackers = None

    with open( csv_file_path, 'r' ) as csv_file:
        current_position = csv_file.tell()
        lineno = 0
        is_next_line_tracker_header = False
        tracker_entry_count = 0
        tracker_header = None
        tracker_data = []
        trackers = {}

        for line in csv_file:
            line = line.strip()
            if not line:
                # An empty line indicates the next line will be a Tracker header.
                is_next_line_tracker_header = True
                tracker_entry_count = 0
            else:
                if is_next_line_tracker_header:
                    is_next_line_tracker_header = False
                    tracker_header = line
                    trackers[ tracker_header ] = []
                    if tracker_found_callback:
                        tracker_found_callback( tracker_header, lineno )
                elif tracker_header:
                    tracker_entry_count += 1
                    trackers[ tracker_header ].append( KeepTrack_CSV_Entry( lineno, line ) )

            lineno += 1

    return trackers

def main():
    arguments = docopt( __doc__, version='KeepTrack v1.0')

    if arguments[ 'trackers' ]:
        def print_tracker_header( tracker_name, lineno=None ):
            if arguments[ '--include-lineno' ]:
                print( '{}: {}'.format( lineno, tracker_name ) )
            else:
                print( '{}'.format( tracker_name ) )
        list_keeptrack_trackers( arguments[ '<keeptrack-csv-file>' ], print_tracker_header )

if __name__ == '__main__':
    main()
