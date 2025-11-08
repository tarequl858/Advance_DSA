# Traversal of Singly Linked List (Iterative Approach) 

class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None 

def traverseList_iterative_approach(head):
    while head is not None:
        print(head.data,end=" ")
        if head.next is not None:
            print(" -> ",end="")
        head = head.next

if __name__ == "__main__":
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)

    traverseList_iterative_approach(head)

# Output: 50  ->  60  ->  20  ->  70
# Time Complexity: O(n)
# Space Complexity: O(1)

# Traversal of Singly Linked List (Recursive Approach)

class Node:
    def __init__ (self,val):
        self.val = val
        self.reference = None

def traverseList_recursive_approach(head):
    if head is not None:
        print(head.val,end=" ")
        if head.reference is not None:
            print(" -> ",end="")
        traverseList_recursive_approach(head.reference)

if __name__ == "__main__":
    head = Node(50)
    head.reference = Node(60)
    head.reference.reference = Node(20)
    head.reference.reference.reference = Node(70)

    traverseList_recursive_approach(head)

# Output: 50  ->  60  ->  20  ->  70
# Time Complexity: O(n)
# Space Complexity: O(n)