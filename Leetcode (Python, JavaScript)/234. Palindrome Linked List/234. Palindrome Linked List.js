/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    let li = []
    let curr = head;
    while (curr!==null){
        li.push(curr.val);
        curr = curr.next;
    }
    let reversedli = [...li].reverse();
    return li.join(',') === reversedli.join(',');
};