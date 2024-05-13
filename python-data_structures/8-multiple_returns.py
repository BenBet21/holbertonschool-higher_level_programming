#!/usr/bin/python3

def multiple_returns(sentence):

    ado = ()
    if len(sentence) == 0:
        ado += (len(sentence), None)
        return ado

    if len(sentence) > 0:
        ado += (len(sentence), sentence[0])
        return ado
