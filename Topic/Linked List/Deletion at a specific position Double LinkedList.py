# Deletion at a specific position in a Doubly Linked List iteratively

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def delete_at_middle(head,pos):
    curr = head
    for i in range(pos-2):
        curr = curr.next
    curr.next = curr.next.next
    curr.next.prev = curr
    return head

def delete_at_middle_iterative_approach(curr):
    while curr is not None:
        print(curr.data,end=" ")
        if curr.next is not None:
            print("->",end="")
        curr = curr.next

if __name__ == "__main__":
    head = Node(50)
    head.next = Node(60)
    head.next.prev = head
    head.next.next = Node(20)
    head.next.next.prev = head.next
    head.next.next.next = Node(70)
    head.next.next.next.prev = head.next.next
    head = delete_at_middle(head,3)
    delete_at_middle_iterative_approach(head)

# Output: 50 ->60 ->70
# Time Complexity: O(n)
# Space Complexity: O(1)

# Deletion at a specific position in a Doubly Linked List recursively

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def delete_at_middle(head,pos):
    curr = head
    for i in range(pos-2):
        curr = curr.next
    curr.next = curr.next.next
    curr.next.prev = curr
    return head

def delete_at_middle_recursive_approach(curr):
    if curr is not None:
        print(curr.data,end=" ")
        if curr.next is not None:
            print("->",end="")
        delete_at_middle_recursive_approach(curr.next)

if __name__ == "__main__":
    head = Node(50)
    head.next = Node(60)
    head.next.prev = head
    head.next.next = Node(20)
    head.next.next.prev = head.next
    head.next.next.next = Node(70)
    head.next.next.next.prev = head.next.next
    head = delete_at_middle(head,3)
    delete_at_middle_recursive_approach(head)

# Output: 50 ->60 ->70
# Time Complexity: O(n)
# Space Complexity: O(1)