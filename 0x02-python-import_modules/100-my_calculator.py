#!/usr/bin/python3
if __name__ == "__main__":
    ''' print sum, sub, mul, div'''
    from calculator_1 import *
    import sys
    args = len(sys.argv) - 1
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = 0
    if sys.argv[2] == "+":
        c = add(a, b)
    elif sys.argv[2] == "-":
        c = sub(a, b)
    elif sys.argv[2] == "*":
        c = mul(a, b)
    else:
        c = div(a, b)
    print("{} {} {} = {}".format(a, sys.argv[2], b, c))
