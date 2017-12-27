'use strict';

class Node {
    constructor(val, next=null) {
        this.val = val;
        this.next = next;
    }
};


class LinkedList {
    constructor(iterable=null) {
        this.head = null;
        this._length = 0;
        if(Array.isArray(iterable)) {
            for (let i = 0; i < iterable.length; i++) {
                this.push(iterable[i]);
            }
        }
    }

    push(val) {
        this.head = new Node(val, this.head);
        this._length++;
    }

    pop() {
        let node = this.head;
        while (node.next.next !== null) {
            node = node.next;
        }
        let popped_val = node.next.val;
        node.next = null;
        this._length--;
        return popped_val;
    }

    size() {
        return this._length;
    }

    search(val) {
        let node = this.head;
        while (node) {
            if (node.val == val) {
                return node;
            }
            node = node.next;
        }
        return null;
    }
};

module.exports = {LinkedList,
                  Node};