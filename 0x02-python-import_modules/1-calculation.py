#!/usr/bin/python2
if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 9 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 9
    b = 4

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))