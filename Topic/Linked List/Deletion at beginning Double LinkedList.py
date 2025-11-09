# Delete a node at the beginning of a doubly linked list iteratively

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def delete_at_start(head):
    curr = head
    curr = curr.next
    curr.prev = None
    return curr

def delete_at_start_iterative_approach(curr):
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
    head = delete_at_start(head)
    delete_at_start_iterative_approach(head)

# Output: 60 -> 20 -> 70
# Time Complexity: O(1)
# Space Complexity: O(1)

# Delete a node at the beginning of a doubly linked list recursively

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def delete_at_start(head):
    curr = head
    curr = curr.next
    curr.prev = None
    return curr

def delete_at_start_recursive_approach(curr):
    if curr is not None:
        print(curr.data,end=" ")
        if curr.next is not None:
            print("->",end="")
        delete_at_start_recursive_approach(curr.next)

if __name__ == "__main__":
    head = Node(50)
    head.next = Node(60)
    head.next.prev = head
    head.next.next = Node(20)
    head.next.next.prev = head.next
    head.next.next.next = Node(70)
    head.next.next.next.prev = head.next.next
    head = delete_at_start(head)
    delete_at_start_recursive_approach(head)

# Output: 60 -> 20 -> 70
# Time Complexity: O(1)
# Space Complexity: O(1)