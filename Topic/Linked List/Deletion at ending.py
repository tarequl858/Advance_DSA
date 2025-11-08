#  Deletion at ending of a linked list iteratively

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def deletion_at_ending_length(head):
    curr = head
    len = 0
    while curr is not None:
        len += 1
        curr = curr.next
    return len

def deletion_at_ending_iterative_approach(head,n):
    curr = head
    for i in range(0,n-2):
        curr = curr.next
    curr.next = None
    while head is not None:
        print(head.data,end=" ")
        if head.next is not None:
            print("->",end="")
        head = head.next

if __name__ == "__main__":
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)
    n = deletion_at_ending_length(head)
    a = deletion_at_ending_iterative_approach(head,n)

# Output: 50 -> 60 -> 20
# Time Complexity: O(n)
# Space Complexity: O(1)

#  Deletion at ending of a linked list recursively

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def deletion_at_ending_length(head):
    curr = head
    len = 0
    while curr is not None:
        len += 1
        curr = curr.next
    return len

def deletion_at_ending_head(head,n):
    curr = head
    for i in range(0,n-2):
        curr = curr.next
    curr.next = None
    return head

def deletion_at_ending_recursive_approach(head):
    if head is not None:
        print(head.data,end=" ")
        if head.next is not None:
            print("->",end="")
        deletion_at_ending_recursive_approach(head.next)

if __name__ == "__main__":
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)
    head = deletion_at_ending_head(head,n)
    deletion_at_ending_recursive_approach(head)

# Output: 50 -> 60 -> 20
# Time Complexity: O(n)
# Space Complexity: O(n)