#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("{} argument: ".format(count))
        print("{}: {}".format(count, sys.argv[1]))
    elif count > 1:
        print("{} arguments: ".format(count))
        for num in range(1, count + 1, 1):
            print("{}: {}".format(num, sys.argv[num]))
