#!/usr/bin/python3
def uppercase(str):
    result = ""
    char = ""

    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".)
    print()
