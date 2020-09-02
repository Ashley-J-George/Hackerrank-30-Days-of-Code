# Day 8: Dictionaries and Maps

# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin

d = dict()
lines = stdin.read().splitlines()
for i in range(1, int(lines[0]) + 1):
    t = lines[i].split()
    d[t[0]] = t[1]

for i in lines[int(lines[0]) + 1:]:
    s = ''
    if i in d.keys():
        s += i + '=' + d[i]
        print(s)
    else:
        print('Not found')

