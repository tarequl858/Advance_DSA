# Insert a Node at Front of Double Linked List interatively

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def insert_at_front(head,data):
    new_node = Node(data)
    new_node.next = head
    head.prev = new_node
    return new_node

def insert_at_front_iterative_approach(curr):
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
    head = insert_at_front(head,new_data)
    insert_at_front_iterative_approach(head)

# Sample Input: 10
# Sample Output: 10 -> 50 -> 60 -> 20 -> 70
# Time Complexity: O(1)
# Space Complexity: O(1)

# Insert a Node at Front of Double Linked List recursively

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def insert_at_front(head,data):
    new_node = Node(data)
    new_node.next = head
    head.prev = new_node
    return new_node

def insert_at_front_recursive_approach(curr):
    if curr is not None:
        print(curr.data,end=" ")
        if curr.next is not None:
            print("->",end="")
        insert_at_front_recursive_approach(curr.next)

if __name__ == "__main__":
    new_data = int(input("Enter a new data: "))
    head = Node(50)
    head.next = Node(60)
    head.next.prev = head
    head.next.next = Node(20)
    head.next.next.prev = head.next
    head.next.next.next = Node(70)
    head.next.next.next.prev = head.next.next
    head = insert_at_front(head,new_data)
    insert_at_front_recursive_approach(head)

# Sample Input: 10
# Sample Output: 10 -> 50 -> 60 -> 20 -> 70
# Time Complexity: O(1)
# Space Complexity: O(1)