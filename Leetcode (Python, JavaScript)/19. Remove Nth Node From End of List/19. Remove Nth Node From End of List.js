/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let curr = head
    let len = 0
    while (curr!=null){
        len += 1
        curr = curr.next
    }
    let curr1 = head
    if (n==len){
        return head.next
    }
    for (i=0;i<len-n-1;i++){
        curr1 = curr1.next
    }
    curr1.next = curr1.next.next
    return head
};