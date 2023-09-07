#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    len1 = len(sys.argv)
    if len1 != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)
    op = sys.argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("{}".format("Unknown operator. Available operators: +, -, * and /"))
        exit(1)
    nu1 = int(sys.argv[1])
    nu2 = int(sys.argv[3])
    if op == '+':
        print("{} + {} = {}".format(nu1, nu2, add(nu1, nu2)))
    elif op == '-':
         print("{} - {} = {}".format(nu1, nu2, sub(nu1, nu2)))
    elif op == '*':
         print("{} * {} = {}".format(nu1, nu2, mul(nu1, nu2)))
    elif op == '/':
         print("{} / {} = {}".format(nu1, nu2, div(nu1, nu2)))

