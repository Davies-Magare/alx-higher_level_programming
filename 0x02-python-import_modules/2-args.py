#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len1 = len(sys.argv)
    if len1 == 1:
        print("{}".format("0 arguments."))
    elif len1 == 2:
        print("{}".format("1 argument:"))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len1 - 1))
        for i in range(1, len1):
            print("{}: {}".format(i, sys.argv[i]))
