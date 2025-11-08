# reverse a linked list iteratively

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse_iterative_approach_head(head):
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    head = prev
    return head

def reverse_iterative_approach(head):
    curr = head
    while curr is not None:
        print(curr.data,end=" ")
        if curr.next is not None:
            print("->",end="")
        curr = curr.next

if __name__ == "__main__":
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)
    head = reverse_iterative_approach_head(head)
    reverse_iterative_approach(head)

# Output: 70 -> 20 -> 60 -> 50
# Time Complexity: O(n)
# Space Complexity: O(1)

# reverse a linked list recursively

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse_recursive_approach_head(head):
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    head = prev
    return head

def reverse_recursive_approach(curr):
    if curr is not None:
        print(curr.data,end=" ")
        if curr.next is not None:
            print("->",end="")
        reverse_recursive_approach(curr.next)

if __name__ == "__main__":
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)
    head = reverse_recursive_approach_head(head)
    reverse_recursive_approach(head)

# Output: 70 -> 20 -> 60 -> 50
# Time Complexity: O(n)
# Space Complexity: O(n)

# reverse a linked list using stack

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse_stack_approach_push_pop(head):
    stack = []
    curr = head
    while curr.next is not None:
        stack.append(curr)
        curr = curr.next
    head = curr
    while stack:
        curr.next = stack.pop()
        curr = curr.next
    curr.next = None
    return head

def reverse_stack_approach(curr):
    while curr is not None:
        print(curr.data,end=" ")
        if curr.next is not None:
            print("->",end="")
        curr = curr.next

if __name__ == "__main__":
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)
    head = reverse_stack_approach_push_pop(head)
    reverse_stack_approach(head)

# Output: 70 -> 20 -> 60 -> 50
# Time Complexity: O(n)
# Space Complexity: O(n)