# Day 25: Running Time and Complexity


# Enter your code here. Read input from STDIN. Print output to STDOUT
def isprime(n):
    if (n <= 1):
        return 'Not prime'
    if (n <= 3):
        return 'Prime'

    if (n % 2 == 0 or n % 3 == 0):
        return 'Not prime'

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return 'Not prime'
        i = i + 6

    return 'Prime'

n = int(input())
l = []

for _ in range(n):
    l.append(int(input()))

for i in range(n):
    l[i] = isprime(l[i])

for i in range(n):
    print(l[i])

