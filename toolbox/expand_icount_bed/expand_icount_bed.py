#!/usr/bin/env python
#-------------------------------------------------------------
# This script takes an 6-column bed file generated by iCount
# and expands it to single features for convenient counting.
#-------------------------------------------------------------
# Thomas Schwarzl <schwarzl@embl.de>
#-------------------------------------------------------------
VERSION = "0.1"

'''

SYNOPSIS

    expand_icount_bed.py [options]

DESCRIPTION


    [-i, --input]
                          BED file for input
                          default: input.bed

    [-v, --version]
                          print the version

    [-h, --help]          display help message with all parameters and options


EXAMPLES

    python expand_icount_bed.py -i counts.bed.gz


AUTHOR

    Thomas Schwarzl <schwarzl@embl.de>

'''

import optparse, traceback, os, time
from pybedtools import BedTool


# =====================================================================================

def main():
    global options, args

    from pybedtools import BedTool

    bed = BedTool(options.input)

    for line in bed:
        for i in range(0,int(line[4])):
            print "\t".join((line[0], line[1], line[2], line[3], str(1), line[5]))

#-------------------------------------------------------------

# Function returns true if the file exists and filename is not empty
def checkFileExists(filename):
   if (notEmpty(filename)):
      parser.error ('%s is not a valid filename' % filename)
   if (os.path.isfile(filename) == False):
      parser.error ('%s does not exist' % filename)

#-------------------------------------------------------------

# Function returns true if filename is not empty
def notEmpty(filename):
   return filename == False or filename == ''

# =====================================================================================
# program can be used as standalone or as module
if __name__ == '__main__':
    try:
        # get parser and add arguments
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'], version="%prog 1.0")

        parser.add_option('-i', '--input', action='store',  type='string', default="input.bed", dest="input", help="input bed file")
        parser.add_option('-v', '--version', action='store_true', default=False,  dest='primary', help='set if you want to use only primary positions of multimapping reads')
        (options, args) = parser.parse_args()

        # check if there are all arguments
        if len(args) != 0:
            parser.error ('Incorrect number of user-specified arguments')

        checkFileExists(options.input)

        # execute main
        main()


    # Exception Handling: Interruption / Errors
    except KeyboardInterrupt, exception: # Control - C
      raise exception
    except SystemExit, exception:
      raise exception
    except Exception, exception:
      print '______________________________[ Error ]______________________________ '
      print str(exception)
      print '____________________________[ Traceback ]____________________________  '
      traceback.print_exc()

      os._exit(1)