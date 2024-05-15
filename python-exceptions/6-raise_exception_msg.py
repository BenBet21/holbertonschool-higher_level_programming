#!/usr/bin/python3

def raise_exception_msg(message=""):

    try:
        eval("non_existent_variable")
    except NameError:
        raise NameError(message)