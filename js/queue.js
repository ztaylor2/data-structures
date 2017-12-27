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
        if (this._length === 1) {
            let val = this.head.val
            this.head = null
            this._length--;
            return val
        }

        let node = this.head
        while (node.next.next) {
            node = node.next;
        }
        let val = node.next.val;
        node.next = null;
        this._length--;
        return val
    }

    peek() {
        if (this._length === 0) {
            throw new Error('List is empty.'); 
        }

        let node = this.head;
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