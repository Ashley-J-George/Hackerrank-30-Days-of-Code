# Day 11: 2D Arrays

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    n, mx, s = 0, -10000000, 0
    i, j, k, l = 0, 1, 2, 0
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    while n < 4:
        while l + 2 < 6:
            s = sum(arr[i][l:l + 3]) + arr[j][l + 1] + sum(arr[k][l:l + 3])
            # print(arr[i][l:l+3], '+', arr[j][l+1], '+', arr[k][l:l+3], '=', s)
            if mx < s:
                mx = s
            l += 1
        l = 0
        i += 1
        j += 1
        k += 1
        n += 1

    print(mx)

