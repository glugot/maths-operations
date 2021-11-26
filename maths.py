#!/usr/bin/env python3

import sys

from operations import add


def main():
    if len(sys.argv) != 3:
        print('Usage: python maths.py <integer 1> <integer>')
    else:
        try:
            number1 = int(sys.argv[1])
            number2 = int(sys.argv[2])
        except ValueError:
            print('Enter two valid integers.')
            sys.exit(1)

        print(add(number1, number2))


if __name__ == '__main__':
    main()
