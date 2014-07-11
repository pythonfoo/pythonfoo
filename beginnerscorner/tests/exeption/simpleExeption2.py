#!/usr/bin/python3
import sys

def throws():
    raise RuntimeError('this is the error message')

def main():
    try:
        throws()
        return 0
# Unterschied Python3 Pyhton2.7
#   except Exception, err:


    except RuntimeError as err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        return 1

if __name__ == '__main__':
    sys.exit(main())
