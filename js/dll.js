'use strict';

class Node {
    constructor(val, next=null, prev=null) {
        this.val = val;
        this.next = next;
        this.prev = prev;
    }
}

class Dll {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(val) {
        if (this.length === 0) {
            this.head = new Node(val);
            this.tail = this.head;
        } else {
            this.head = new Node(val, this.head);
            this.head.next.prev = this.head;
        }
        this.length++;
    }

    append(val) {
        if (this.length === 0) {
            this.tail = new Node(val);
            this.head = this.tail;
        } else {
            this.tail = new Node(val, null, this.tail);
            this.tail.prev.next = this.tail;
        }
        this.length++;
    }

    pop() {

    }

    shift() {

    }

    remove() {

    }
}

module.exports = {Dll}