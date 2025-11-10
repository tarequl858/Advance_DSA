# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        len = 0
        while curr is not None:
            len += 1
            curr = curr.next
        curr = head
        if n==len:
            return head.next
        for i in range(len-n-1):
            curr = curr.next
        curr.next = curr.next.next
        return head