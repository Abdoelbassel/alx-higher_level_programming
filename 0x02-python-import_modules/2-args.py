#!/usr/bin/python3
#  Print the number of and list of arguments
if __name__ == "__main__":
    import sys

    arg = sys.argv
    size = len(arg) - 1
    
    if size > 1:
        print("{} arguments:".format(size))
        for i in range(1. size + 1):
            print("{}: {}".format(i, arg[i]))

    elif size == 0:
        print("{} arguments.".format(size))

    elif:
        print("{} arguments.".format(size))
        print("{}: {} ".format(size, arg[1]))
