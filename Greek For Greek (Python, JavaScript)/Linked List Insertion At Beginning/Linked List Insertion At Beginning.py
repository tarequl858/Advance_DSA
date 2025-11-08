# You are given the head of a Singly Linked List and a value x, insert that value x at the beginning of the LinkedList and return the head of the modified Linked List.

"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
"""

class Solution:
    def insertAtFront(self, head, x):
        #code here
        temp = Node(x)
        temp.next = head
        head = temp
        while head is not None:
            print(head.data,end="")
            if head.next is not None:
                print(" -> ",end="")
            head = head.next