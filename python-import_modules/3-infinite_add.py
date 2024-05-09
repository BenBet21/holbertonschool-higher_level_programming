#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    addition = 0

    if len(arguments) == 1:
        print("0".format(arguments))

    if len(arguments) == 2:
        for index, arg in enumerate(arguments[1:], start=1):
            print("{}".format(arg))

    if len(arguments) > 2:
        for index, arg in enumerate(arguments[1:], start=1):
            addition += int(arg)
        print("{}".format(addition))
