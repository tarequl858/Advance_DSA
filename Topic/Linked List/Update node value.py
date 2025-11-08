#  Update Node Data in a Linked List Iteratively

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def update_node_at_point(head, pos, new_data):
    curr = head
    count = 1
    while curr is not None:
        if count == pos:
            curr.data = new_data
            return head
        curr = curr.next
        count += 1
    return head

def update_node_at_point_iterative_approach(curr):
    while curr is not None:
        print(curr.data,end=" ")
        if curr.next is not None:
            print("->",end="")
        curr = curr.next

if __name__ == "__main__":
    pos = int(input("Enter positon number: "))
    new_data = int(input("Enter new number: "))
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)
    head = update_node_at_point(head, pos, new_data)
    update_node_at_point_iterative_approach(head)

# Output: 50 -> 99 -> 20 -> 70  (if pos=2 and new_data=99)
# Time Complexity: O(n)
# Space Complexity: O(1)

#  Update Node Data in a Linked List Recursively

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def update_node_recursive(head, pos, new_data):
    if head is None:
        return None
    if pos == 1:
        head.data = new_data
        return head
    update_node_recursive(head.next, pos-1, new_data)
    return head

def update_node_at_point_recursive_approach(curr):
    while curr is not None:
        print(curr.data,end=" ")
        if curr.next is not None:
            print("->",end="")
        curr = curr.next

if __name__ == "__main__":
    pos = int(input("Enter positon number: "))
    new_data = int(input("Enter new number: "))
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)
    head = update_node_recursive(head, pos, new_data)
    update_node_at_point_recursive_approach(head)

# Output: 50 -> 99 -> 20 -> 70  (if pos=2 and new_data=99)
# Time Complexity: O(n)
# Space Complexity: O(n)