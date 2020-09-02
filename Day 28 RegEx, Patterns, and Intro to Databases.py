# Day 28: RegEx, Patterns, and Intro to Databases


# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
N = int(input())
l = []

for N_itr in range(N):
    firstNameEmailID = input().split()

    firstName = firstNameEmailID[0]

    emailID = firstNameEmailID[1]

    if emailID.endswith('@gmail.com'):
        l.append(firstName)

l.sort()

for i in l:
    print(i)


