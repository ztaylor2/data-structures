'use strict';

class Node {
    constructor(val, next=null) {
        this.val = val;
        this.next = next;
    }
};

class Queue {
    constructor() {
        this.head = null;
        this._length = 0;
    }

    enqueue(val) {
        this.head = new Node(val, this.head)
        this._length++;
    }

    dequeue() {
        if (this._length === 0) {
            throw new Error('List is empty.'); 
        }
        this._length--;
    }

    peek() {
        if (this._length === 0) {
            throw new Error('List is empty.'); 
        }

        let node = self.head;
        while (node.next) {
            node = node.next;
        }

        return node.val
    }

    size() {
        return this._length
    }
}

module.exports = {Queue,
                  Node};