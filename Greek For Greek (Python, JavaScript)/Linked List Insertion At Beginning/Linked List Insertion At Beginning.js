// You are given the head of a Singly Linked List and a value x, insert that value x at the beginning of the LinkedList and return the head of the modified Linked List.


/*
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}
*/

class Solution {
    insertAtFront(head, x) {
        // Code here
        let temp = new Node(x);
        temp.next = head;
        head = temp;
        while (head !== null){
            process.stdout.write(head.data.toString());
            if (head.next !== null){
                process.stdout.write(" -> ");
            }
            head = head.next;
        }return head;
    }
}