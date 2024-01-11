#!/usr/bin/python3

def roman_to_int(roman_string):
    """roman_to_int: converts a Roman numeral to an integer

    Args:
        roman_string:

    Returns:
        converted integer
    """
    ret = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return ret
    I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
    indicator = False
    for i in range(len(roman_string)):
        if indicator:
            indicator = False
            continue
        if roman_string[i] == 'I':
            if (i + 1) < len(roman_string):
                if (roman_string[i + 1] == 'V'):
                    ret += 4
                    indicator = True
                    continue
                elif (roman_string[i + 1]) == 'X':
                    ret += 9
                    indicator = True
                    continue
            ret += 1
            continue
        elif roman_string[i] == 'V':
            ret += 5
        elif roman_string[i] == 'X':
            if (i + 1) < len(roman_string):
                if (roman_string[i + 1] == 'L'):
                    ret += 40
                    indicator = True
                    continue
                elif (roman_string[i + 1]) == 'C':
                    ret += 90
                    indicator = True
                    continue
            ret += 10
            continue
        elif roman_string[i] == 'L':
            ret += 50
            continue
        elif roman_string[i] == 'C':
            if (i + 1) < len(roman_string):
                if (roman_string[i + 1] == 'D'):
                    ret += 400
                    indicator = True
                    continue
                elif (roman_string[i + 1]) == 'M':
                    ret += 900
                    indicator = True
                    continue
            ret += 100
            continue
        elif roman_string[i] == 'D':
            ret += 500
            continue
        elif roman_string[i] == 'M':
            ret += 1000
    return ret
