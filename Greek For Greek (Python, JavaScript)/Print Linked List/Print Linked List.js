// You are given the head of a singly linked list. Return an array containing the values of the nodes.

/*
class Node {
  constructor(x){
    this.data = x;
    this.next = null;
  }
}

/**
 * @param {Node} head
 */
class Solution {
    printList(head) {
        // code here
        let arr = [];
        let temp = head;
        while (temp !== null){
            arr.push(temp.data);
            temp = temp.next;
        }
        return arr;
    }
}