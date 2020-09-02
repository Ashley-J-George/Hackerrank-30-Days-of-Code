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

