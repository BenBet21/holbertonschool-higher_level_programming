#!/usr/bin/python3
def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    dict_romain = {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'M': 1000,
                   'D': 500}
    result = 0

    for symb in roman_string:
        if symb == dict_romain:
            result += dict_romain[symb]

    for i in range(len(roman_string) - 1):
        val_actuelle = dict_romain[roman_string[i]]
        val_suivante = dict_romain[roman_string[i + 1]]

        if val_actuelle < val_suivante:
            result -= val_actuelle
        else:
            result += val_actuelle
    result += dict_romain[roman_string[-1]]

    return result
