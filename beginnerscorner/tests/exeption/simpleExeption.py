#!/usr/bin/python3
# Einfachste Form einer Exeption


def throws():
    raise RuntimeError('this is the error message')

def main():
    throws()

if __name__ == '__main__':
    main()
