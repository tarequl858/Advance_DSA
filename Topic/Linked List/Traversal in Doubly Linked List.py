# Traversal in Doubly Linked List iteratively

class Node:
    def __init__ (self,data):
        self.data = data
        self.prev = None
        self.next = None

def forward_traversal(head):
    forward_array = []
    curr = head
    while curr is not None:
        forward_array.append(curr.data)
        curr = curr.next
    backward_array = []
    backward_array = forward_array[::-1]
    return forward_array, backward_array

if __name__ == "__main__":
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)

    fwd, bwd = forward_traversal(head)
    print(fwd)
    print(bwd)

# Output: [50, 60, 20, 70]
# Output: [70, 20, 60, 50]
# Time Complexity: O(n)
# Space Complexity: O(n)

# Traversal in Doubly Linked List iteratively

class Node:
    def __init__ (self,data):
        self.data = data
        self.prev = None
        self.next = None

def forward_traversal(head):
    forward_array = []
    curr = head
    while curr is not None:
        forward_array.append(curr.data)
        curr = curr.next
    backward_array = []
    while head is not None:
        backward_array.insert(0,head.data)
        head = head.next
    return forward_array, backward_array

if __name__ == "__main__":
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)

    fwd, bwd = forward_traversal(head)
    print(fwd)
    print(bwd)

# Output: [50, 60, 20, 70]
# Output: [70, 20, 60, 50]
# Time Complexity: O(n)
# Space Complexity: O(n)

# Traversal in Doubly Linked List using deque

class Node:
    def __init__ (self,data):
        self.data = data
        self.prev = None
        self.next = None

from collections import deque
def displayList(head):
    forward_array = []
    backward_array = deque()
    curr = head
    while curr is not None:
        forward_array.append(curr.data)
        backward_array.appendleft(curr.data)
        curr = curr.next
    return forward_array, list(backward_array)

if __name__ == "__main__":
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)

    fwd, bwd = displayList(head)
    print(fwd)
    print(bwd)

# Output: [50, 60, 20, 70]
# Output: [70, 20, 60, 50]
# Time Complexity: O(n)
# Space Complexity: O(n)

# Traversal in Doubly Linked List using recursion

class Node:
    def __init__ (self,data):
        self.data = data
        self.prev = None
        self.next = None

def forward_recursive(curr):
    if curr is not None:
        print(curr.data,end=" ")
        forward_traversal(curr.next)

def backward_recursive(curr):
    if curr is not None:
        print(curr.data,end=" ")
        backward_traversal(curr.prev)

if __name__ == "__main__":
    head = Node(50)
    head.next = Node(60)
    head.next.prev = head
    head.next.next = Node(20)
    head.next.next.prev = head.next
    head.next.next.next = Node(70)
    head.next.next.next.prev = head.next.next
    tail = head.next.next.next
    forward_recursive(head)
    print()
    backward_recursive(tail)

# Output: 50 60 20 70
# Output: 70 20 60 50
# Time Complexity: O(n)
# Space Complexity: O(n)