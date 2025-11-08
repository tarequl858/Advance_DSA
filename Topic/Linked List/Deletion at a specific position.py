# delete_at_specific_point_iterative_approach

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_at_specific_point_head(head,n):
    curr = head
    for i in range(0,n-2):
        curr = curr.next
    curr.next = curr.next.next
    return head

def delete_at_specific_point_iterative_approach(head):
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
    head = delete_at_specific_point_head(head,3)
    delete_at_specific_point_iterative_approach(head)

# Output: 50 -> 60 -> 70
# Time Complexity: O(n)
# Space Complexity: O(1)

# delete_at_specific_point_recursive_approach

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_at_specific_point_head(head,n):
    curr = head
    for i in range(0,n-2):
        curr = curr.next
    curr.next = curr.next.next
    return head

def delete_at_specific_point_recursive_approach(head):
    if head is not None:
        print(head.data,end=" ")
        if head.next is not None:
            print("->",end="")
        delete_at_specific_point_recursive_approach(head.next)

if __name__ == "__main__":
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)
    head = delete_at_specific_point_head(head,3)
    delete_at_specific_point_recursive_approach(head)

# Output: 50 -> 60 -> 70
# Time Complexity: O(n)
# Space Complexity: O(n)