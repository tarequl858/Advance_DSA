# Add a new node at the beginning of the linked list iteratively

class Node:
    def __init__ (self,value):
        self.data = value
        self.next = None

def add_beginning_iterative_approach(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    head = new_node
    while head is not None:
        print(head.data,end=" ")
        if head.next is not None:
            print(" -> ",end="")
        head = head.next

if __name__ == "__main__":
    new_data = 30
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)

    add_beginning_iterative_approach(head,new_data)

# Output: 30  ->  50  ->  60  ->  20  ->  70
# Time Complexity: O(n)
# Space Complexity: O(1)

# Adding a new node at the beginning of the linked list recursively

class Node:
    def __init__ (self,value):
        self.data = value
        self.next = None

def add_beginning_head(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    head = new_node
    return head
    
def add_beginning_recursive_approach(head):
    if head is not None:
        print(head.data,end=" ")
        if head.next is not None:
            print(" -> ",end="")
        add_beginning_recursive_approach(head.next)

if __name__ == "__main__":
    new_node = 30
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)
    head = add_beginning_head(head,new_node)
    add_beginning_recursive_approach(head)

# Output: 30  ->  50  ->  60  ->  20  ->  70
# Time Complexity: O(n)
# Space Complexity: O(n)