#!/usr/bin/env python3

import argparse

from operations import add, subtract, divide, multiply


def main():
    parser = argparse.ArgumentParser(
        description="Perform simple mathematical operations on 2 integers."
    )
    parser.add_argument(
        'operation',
        choices=['add', 'subtract', 'multiply', 'divide'],
        help='The mathematical operation to perform.'
    )
    parser.add_argument(
        'number1',
        type=int,
        help="The first operand"
    )
    parser.add_argument(
        'number2',
        type=int,
        help="The second operand"
    )

    args = parser.parse_args()

    if args.operation == 'add':
        result = add(args.number1, args.number2)
    elif args.operation == 'subtract':
        result = subtract(args.number1, args.number2)
    elif args.operation == 'divide':
        result = divide(args.number1, args.number2)
    elif args.operation == 'multiply':
        result = multiply(args.number1, args.number2)
    else:
        raise NotImplementedError(
            'The {} operation has not been implemented yet.'.format(
                args.operation
            )
        )
    print(result)


if __name__ == '__main__':
    main()
