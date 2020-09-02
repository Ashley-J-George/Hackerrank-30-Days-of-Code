# Day 0: Hello, World.

# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')

# TODO: Write a line of code here that prints the contents of input_string to stdout.

print(input_string)

'''######################################################################################################'''

# Day 1: Data Types



# Declare second integer, double, and String variables.
n = 0
f = 0.0
ss = ''
# Read and save an integer, double, and String to your variables.
n = int(input())
f = float(input())
ss = input()
# Print the sum of both integer variables on a new line.
print(n + i)
# Print the sum of the double variables on a new line.
print(f + d)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + ss)

'''######################################################################################################'''

# Day 2: Operators


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    print(round(meal_cost + tip + tax))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

'''######################################################################################################'''

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

'''#######################################################################################################'''

# Day 9: Recursion 3

rec
wala
code
likh

int
main()
{
    int
n, fact = 1, i;
cin >> n;
for (i = 1;
i <= n;
i + +)
fact *= i;

cout << fact;

return 0;
}


'''#######################################################################################################'''

# Day 10: Binary Numbers


# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

count = 0
while n:
    n &= n << 1
    count += 1

print(count)

'''#######################################################################################################'''

# Day 11: 2D Arrays


# !/bin/python3

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

'''#######################################################################################################'''


# Day 12: Inheritance

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

        #   Function Name: calculate
        #   Return: A character denoting the grade.
        #
        # Write your function here

    def calculate(self):
        s = sum(self.scores) / len(self.scores)
        if s >= 90:
            return ('O')
        elif s >= 80:
            return ('E')
        elif s >= 70:
            return ('A')
        elif s >= 55:
            return ('P')
        elif s >= 40:
            return ('D')
        else:
            return ('T')


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

'''#######################################################################################################'''

# Day 13: Abstract Classes


from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(): pass


# Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print('Title:', self.title)
        print('Author:', self.author)
        print('Price:', self.price)


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()

'''#######################################################################################################'''


# Day 14: Scope


class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        i = 0
        self.maximumDifference = 0
        while i < len(self.__elements):
            j = i + 1
            while j < len(self.__elements):
                a = abs(self.__elements[i] - self.__elements[j])
                if a > self.maximumDifference:
                    self.maximumDifference = a
                j += 1
            i += 1


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

'''#######################################################################################################'''


# Day 15: Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Complete this method
        if head == None:
            return Node(data)
        else:
            current = head
            while current.next != None:
                current = current.next
            current.next = Node(data)
            return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head);

'''#######################################################################################################'''

# Day 16: Exceptions - String to Integer


# !/bin/python3
import sys

S = input().strip()

try:
    s = int(S)
    print(s)
except:
    print('Bad String')

'''#######################################################################################################'''


# Day 17: More Exceptions



# Write your code here
class Calculator:
    def power(self, a, b):
        if a < 0 or b < 0:
            raise Exception('n and p should be non-negative')
        else:
            return a ** b


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)

'''#######################################################################################################'''

# Day 18: Queues and Stacks



import sys


class Solution:
    # Write your code here
    def __init__(self):
        self.s = []
        self.q = []

    def pushCharacter(self, a):
        self.s.append(a)

    def enqueueCharacter(self, a):
        self.q.append(a)

    def popCharacter(self):
        return self.s.pop()

    def dequeueCharacter(self):
        return self.q.pop(0)


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")

'''#######################################################################################################'''


# Day 19: Interfaces


class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        s = 0
        for i in range(1, n + 1):
            if n % i == 0:
                s += i
        return s


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

'''#######################################################################################################'''

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

'''#######################################################################################################'''

# Day 21: Generics



# include <iostream>
# include <vector>
# include <string>

using
namespace
std;

/ **
*Name: printArray
*Print
each
element
of
the
generic
vector
on
a
new
line.Do
not
return anything.
* @ param
A
generic
vector
** /

// Write
your
code
here

template <


class T>


void
printArray(vector < T > vec)
{
for (int i=0; i < vec.size(); i++)
cout << vec[i] << endl;
}

int
main()
{
    int
n;

cin >> n;
vector < int > int_vector(n);
for (int
i = 0;
i < n;
i + +) {
    int
value;
cin >> value;
int_vector[i] = value;
}

cin >> n;
vector < string > string_vector(n);
for (int
i = 0;
i < n;
i + +) {
    string
value;
cin >> value;
string_vector[i] = value;
}

printArray < int > (int_vector);
printArray < string > (string_vector);

return 0;
}


'''#######################################################################################################'''



# Day 22: Binary Search Trees


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        # Write your code here
        if root == None:
            return -1
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)

'''#######################################################################################################'''

# Day 23: BST Level-Order Traversal



import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        # Write your code here
        l = []
        n = []
        if root == None:
            return -1
        n.append(root)
        while len(n) != 0:
            t = n.pop(0)
            l.append(t.data)
            if t.left != None:
                n.append(t.left)
            if t.right != None:
                n.append(t.right)

        for i in l:
            print(i, end= ' ')

        T = int(input())
        myTree = Solution()
        root = None
        for i in range(T):
            data = int(input())
            root = myTree.insert(root, data)
        myTree.levelOrder(root)

        '''#######################################################################################################'''

        # Day 24: More Linked Lists



        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None

        class Solution:
            def insert(self, head, data):
                p = Node(data)
                if head == None:
                    head = p
                elif head.next == None:
                    head.next = p
                else:
                    start = head
                    while (start.next != None):
                        start = start.next
                    start.next = p
                return head

            def display(self, head):
                current = head
                while current:
                    print(current.data, end=' ')
                    current = current.next

            def removeDuplicates(self, head):
                # Write your code here
                current = head
                while current.next != None:
                    if current.data != current.next.data:
                        current = current.next
                    else:
                        current.next = current.next.next

                return head

        mylist = Solution()
        T = int(input())
        head = None
        for i in range(T):
            data = int(input())
            head = mylist.insert(head, data)
        head = mylist.removeDuplicates(head)
        mylist.display(head)

        '''#######################################################################################################'''

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

        '''#######################################################################################################'''

        # Day 26: Nested Logic


        rd, rm, ry = [int(x) for x in input().split(' ')]
        ed, em, ey = [int(x) for x in input().split(' ')]

        if (ry, rm, rd) <= (ey, em, ed):
            print(0)
        elif (ry, rm) == (ey, em):
            print(15 * (rd - ed))
        elif ry == ey:
            print(500 * (rm - em))
        else:
            print(10000)

        '''#######################################################################################################'''

        # Day 27: Testing


        def minimum_index(seq):
            if len(seq) == 0:
                raise ValueError("Cannot get the minimum value index from an empty sequence")
            min_idx = 0
            for i in range(1, len(seq)):
                if seq[i] < seq[min_idx]:
                    min_idx = i
            return min_idx

        class TestDataEmptyArray(object):

            @staticmethod
            def get_array():
                # complete this function
                return []

        class TestDataUniqueValues(object):

            @staticmethod
            def get_array():
                # complete this function
                return [2, 5, 6, 1, 0, 7, 8, 9, 3, 4]

            @staticmethod
            def get_expected_result():
                # complete this function
                return 4

        class TestDataExactlyTwoDifferentMinimums(object):

            @staticmethod
            def get_array():
                # complete this function
                return [2, 5, 6, 1, 9, 7, 8, 0, 3, 4, 0]

            @staticmethod
            def get_expected_result():
                # complete this function
                return 7

        def TestWithEmptyArray():
            try:
                seq = TestDataEmptyArray.get_array()
                result = minimum_index(seq)
            except ValueError as e:
                pass
            else:
                assert False

        def TestWithUniqueValues():
            seq = TestDataUniqueValues.get_array()
            assert len(seq) >= 2

            assert len(list(set(seq))) == len(seq)

            expected_result = TestDataUniqueValues.get_expected_result()
            result = minimum_index(seq)
            assert result == expected_result

        def TestiWithExactyTwoDifferentMinimums():
            seq = TestDataExactlyTwoDifferentMinimums.get_array()
            assert len(seq) >= 2
            tmp = sorted(seq)
            assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

            expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
            result = minimum_index(seq)
            assert result == expected_result

        TestWithEmptyArray()
        TestWithUniqueValues()
        TestiWithExactyTwoDifferentMinimums()
        print("OK")

        '''#######################################################################################################'''

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

        '''#######################################################################################################'''

        # Day 29: Bitwise AND



        # !/bin/python3

        import math
        import os
        import random
        import re
        import sys

        if __name__ == '__main__':
            T = int(input().strip())
            for _ in range(T):
                n, k = map(int, input().split())
                print(k - 1 if ((k - 1) | k) <= n else k - 2)
