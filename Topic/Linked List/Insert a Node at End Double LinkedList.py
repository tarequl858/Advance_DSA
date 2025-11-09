# Inset a node at the end of a doubly linked list iteratively

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def insert_at_end(head,data):
    new_node = Node(data)
    curr = head
    while curr.next is not None:
        curr = curr.next
    new_node.prev = curr
    curr.next = new_node
    return head

def insert_at_end_iterative_approach(curr):
    while curr is not None:
        print(curr.data,end=" ")
        if curr.next is not None:
            print("->",end="")
        curr = curr.next

if __name__ == "__main__":
    new_data = int(input("Enter a new data: "))
    head = Node(50)
    head.next = Node(60)
    head.next.prev = head
    head.next.next = Node(20)
    head.next.next.prev = head.next
    head.next.next.next = Node(70)
    head.next.next.next.prev = head.next.next
    head = insert_at_end(head,new_data)
    insert_at_end_iterative_approach(head)

# Sample Input: 80
# Sample Output: 50 -> 60 -> 20 -> 70 -> 80
# Time Complexity: O(n)
# Space Complexity: O(1)

# Insert a Node at End of Double Linked List recursively

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def insert_at_end(head,data):
    new_node = Node(data)
    curr = head
    while curr.next is not None:
        curr = curr.next
    new_node.prev = curr
    curr.next = new_node
    return head

def insert_at_end_recursive_approach(curr):
    if curr is not None:
        print(curr.data,end=" ")
        if curr.next is not None:
            print("->",end="")
        insert_at_end_recursive_approach(curr.next)

if __name__ == "__main__":
    new_data = int(input("Enter a new data: "))
    head = Node(50)
    head.next = Node(60)
    head.next.prev = head
    head.next.next = Node(20)
    head.next.next.prev = head.next
    head.next.next.next = Node(70)
    head.next.next.next.prev = head.next.next
    head = insert_at_end(head,new_data)
    insert_at_end_recursive_approach(head)

# Sample Input: 80
# Sample Output: 50 -> 60 -> 20 -> 70 -> 80
# Time Complexity: O(n)
# Space Complexity: O(n)