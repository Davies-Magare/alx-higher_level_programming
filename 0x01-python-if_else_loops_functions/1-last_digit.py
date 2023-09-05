#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = number
if temp < 0:
    temp *= -1
str1 = "Last digit of "
last = temp % 10
if number < 0:
    last *= -1
if last > 5:
    print(f"{str1}{number} is {last} and is greater than 5")
elif last == 0:
    print(f"{str1}{number} is {last} and is 0")
elif last < 6 and last != 0:
    print(f"{str1}{number} is {last} and is less than 6 and not 0")
