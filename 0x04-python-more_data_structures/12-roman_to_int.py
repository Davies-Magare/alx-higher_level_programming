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
            'M': 1000,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
            'IV': 4,
            'IX': 9
        }
    number = 0
    i = 0
    while i < len(rom_str):
        redc = ""
        flag = 0
        if i < (len(rom_str) - 1):
            if (rom_str[i] == 'X' or rom_str[i] == 'C'
                    or rom_str[i] == 'I'):
                redc += rom_str[i]
                redc += rom_str[i + 1]
                for item in d:
                    if item == redc:
                        number += d[redc]
                        i += 2
                        flag = 1
        if flag:
            continue
        number += d[rom_str[i]]
        i += 1
    return number
