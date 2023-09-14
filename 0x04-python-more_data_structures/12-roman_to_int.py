#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string is None:
        return 0
    rom_str = roman_string
    d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    number = 0
    i = 0
    while i < len(rom_str):
        number += d[rom_str[i]]
        if i > 0:
            if rom_str[i] == 'X' and rom_str[i - 1] == 'I':
                number -= 2
            elif rom_str[i] == 'V' and rom_str[i - 1] == 'I':
                number -= 2
        i += 1
    return number
