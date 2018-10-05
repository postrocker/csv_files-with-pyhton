#!/usr/bin/python3

import csv  # module for csv files
import argparse

def main():

    # External arguments
    parser = argparse.ArgumentParser( description="Stelios's awesome programm!!!!" )
    parser.add_argument( "-f", "--filepath",
                         help = "Select the input file path",
                         required = True )
    args = parser.parse_args()

    # create empty lists
    kwh = []
    ahm = []

    # opens file and stores data into the empty lists
    filename = args.filepath
    print( "User gave the file: " + str( filename ) )

    with open( filename ) as csv_file:
        csv_reader = csv.reader( csv_file )  # the reader

        for row in csv_reader:                # loop in order to take first line of data
            kwh.append( row[0] )             # storing data in empty lists
            ahm.append( row[1] )

        # the filter (set() randomises data, used list(dict.fromkeys()) instead)
        filtered_kwh = list( dict.fromkeys( kwh ) )
        filtered_ahm = list( dict.fromkeys( ahm ) )

        # join two lists into one
        filtered_kwh_ahm = zip( filtered_kwh, filtered_ahm )

        # creates new csv file and writes the filtered data
        with open("new_" + filename, 'w', newline='') as new_csv_file:
            csv_writer = csv.writer( new_csv_file )

            for row in filtered_kwh_ahm:      # loop over new file writing new data
                csv_writer.writerow( row )

    print("new_" + str(filename) + " was created")

if __name__== "__main__":
    main()
