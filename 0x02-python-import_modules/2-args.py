#!/usr/bin/python3
if __name__ == "__main__":
    import sys
if (len(sys.argv) == 1):
    print("0 arguments.")
else:
    print("{:d} arguments:".format(len(sys.argv) - 1))
    for i in range(2, len(sys.argv) + 1):
        print("{:d}: {}".format(i - 1, sys.argv[i - 1]))
