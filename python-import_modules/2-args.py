#!/usr/bin/python3
import sys
arguments = sys.argv

if len(arguments) == 1:
    print("0 arguments.".format(arguments))

if len(arguments) == 2:
    print("{} argument:".format(len(arguments) - 1))
    for index, arg in enumerate(arguments[1:], start=1):        
        print("{}: {}".format(index, arg))

if len(arguments) > 2:    
    print("{} arguments:".format(len(arguments) - 1))
    for index, arg in enumerate(arguments[1:], start=1):        
        print("{}: {}".format(index, arg))
