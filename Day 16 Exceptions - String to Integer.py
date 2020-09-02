# Day 16: Exceptions - String to Integer


# !/bin/python3
import sys

S = input().strip()

try:
    s = int(S)
    print(s)
except:
    print('Bad String')

