# Add Ending a new node at the end of the linked list iteratively

class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = self.tail = None

def add_end_iterative_approach(head,tail, new_data):
    new_node = Node(new_data)
    tail.next = new_node
    tail = new_node
    while head is not None:
        print(head.data,end=" ")
        if head.next is not None:
            print(" -> ",end="")
        head = head.next

if __name__ == "__main__":
    new_data = 10
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)
    tail = head.next.next.next

    add_end_iterative_approach(head,tail,new_data)

# Output: 50  ->  60  ->  20  ->  70  ->  10
# Time Complexity: O(n)
# Space Complexity: O(1)

# Adding a new node at the end of the linked list recursively

class Node:
    def __init__ (self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = self.tail = None

def add_end_head(tail,new_data):
    new_node = Node(new_data)
    tail.next = new_node
    tail = new_node
    return tail

def add_end_recursive_approach(head):
    if head is not None:
        print(head.val,end=" ")
        if head.next is not None:
            print(" -> ",end="")
        add_end_recursive_approach(head.next)

if __name__ == "__main__":
    new_data = 10
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)
    tail = head.next.next.next
    tail = add_end_head(tail,new_data)
    add_end_recursive_approach(head)

# Output: 50  ->  60  ->  20  ->  70  ->  10  
# Time Complexity: O(n)
# Space Complexity: O(n)  