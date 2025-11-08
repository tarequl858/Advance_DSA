# Search an element in a linked list iteratively

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def search_an_element_iterative_approach(head,key):
    symbol = False
    while head is not None:
        if head.data == key:
            symbol = True
            break
        else:
            symbol = False
        head = head.next
    print(symbol)

if __name__ == "__main__":
    key = int(input("Enter key for searching: "))
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)
    search_an_element_iterative_approach(head,key)

# Output: True/False based on key presence
# Time Complexity: O(n)
# Space Complexity: O(1)

# Search an element in a linked list recursively

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def search_an_element_recursive_approach(head, key):
    if head is None:
        return False
    if head.data == key:
        return True
    return search_an_element_recursive_approach(head.next, key)

if __name__ == "__main__":
    key = int(input("Enter key for searching: "))
    head = Node(50)
    head.next = Node(60)
    head.next.next = Node(20)
    head.next.next.next = Node(70)
    print(search_an_element_recursive_approach(head,key))

# Output: True/False based on key presence
# Time Complexity: O(n)
# Space Complexity: O(n)