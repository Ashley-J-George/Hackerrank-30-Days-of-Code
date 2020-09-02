# Day 20: Sorting


# !/bin/python3

import sys


def swap(a, b):
    t = a
    a = b
    b = t
    return (a, b)


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numberOfSwaps = 0
# Write Your Code Here
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = swap(a[j], a[j + 1])
            numberOfSwaps += 1
    if numberOfSwaps == 0:
        break

print ('Array is sorted in', numberOfSwaps, 'swaps.')
print ('First Element:', a[0])
print ('Last Element:', a[len(a) - 1])

