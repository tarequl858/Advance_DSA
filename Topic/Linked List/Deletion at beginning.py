#  Deletion at beginning of a linked list iteratively

class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

def deletion_at_beginning_iteratice_approach(head):
    head = head.next
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

    deletion_at_beginning_iteratice_approach(head)

# Output: 60 -> 20 -> 70

# Time Complexity: O(n)
# Space Complexity: O(1)

#  Deletion at beginning of a linked list recursively

class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

def deletion_at_beginning_head(head):
    head = head.next
    return head

def deletion_at_beginning_iteratice_approach(head):
    if head is not None:
        print(head.data,end=" ")
        if head.next is not None:
            print("->",end="")
        deletion_at_beginning_iteratice_approach(head.next)

if __name__ == "__main__":
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)
    head = deletion_at_beginning_head(head)
    deletion_at_beginning_iteratice_approach(head)

# Output: 60 -> 20 -> 70
# Time Complexity: O(n)
# Space Complexity: O(n)