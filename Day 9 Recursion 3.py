# Day 9: Recursion 3


def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


print(factorial(int(input())))
