# You are given the head of a singly linked list. Return an array containing the values of the nodes.

'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def printList(self, head):
        # code here
        li = []
        temp = head
        while temp is not None:
            li.append(temp.data)
            temp = temp.next
        return li