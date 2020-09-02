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

