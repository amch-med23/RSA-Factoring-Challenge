#!/usr/bin/python3
import sys


def factorize(number):
    """ Generate 2 factors for a given number"""
    fact1 = 2
    while (number % fact1):
        if (fact1 <= number):
            fact1 += 1

    fact2 = number // fact1
    return (fact2, fact1)


if len(sys.argv) != 2:
    sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

supplied_file = sys.argv[1]

file = open(supplied_file, 'r')
lines = file.readlines()

for line in lines:
    number = int(line.rstrip())
    fact2, fact1 = factorize(number)
    print(f"{number} = {fact2} * {fact1}")
