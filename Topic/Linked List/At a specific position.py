# Insert a node at a specific position in a linked list iteratively

class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

def middle_point_iterative_approach(head,n,new_node):
    curr = head
    for i in range(0,n-2):
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    while head is not None:
        print(head.data,end=" ")
        if head.next is not None:
            print(" -> ",end="")
        head = head.next

if __name__ == "__main__":
    new_node = Node(30)
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)

    middle_point_iterative_approach(head,3,new_node)

# Output: 50  ->  60  ->  30  ->  20  ->  70
# Time Complexity: O(n)
# Space Complexity: O(1)

# Insert a node at a specific position in a linked list recursively

class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

def middle_point_head(head,n,new_node):
    curr = head
    for i in range(0,n-1):
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    return head

def middle_point_recursive_approach(head):
    if head is not None:
        print(head.data,end=" ")
        if head.next is not None:
            print("->",end="")
        middle_point_recursive_approach(head.next)

if __name__ == "__main__":
    new_node = Node(30)
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)

    head = middle_point_head(head,3,new_node)
    middle_point_recursive_approach(head)

# Output: 50 ->60 ->20 ->30 ->70
# Time Complexity: O(n)
# Space Complexity: O(n)