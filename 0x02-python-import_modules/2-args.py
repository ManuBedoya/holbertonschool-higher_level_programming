#!/usr/bin/python3
if __name__ == "__main__":
    import sys
if (len(sys.argv) == 1):
    print("0 arguments:")
elif (len(sys.argv) == 2):
    print("1 argument:\n1: {}".format(sys.argv[1]))
else:
    print("{:d} arguments:".format(len(sys.argv)))
    for i in range(2, len(sys.argv) + 1):
        print("{:d}: {}".format(i, sys.argv[i - 1]))
