'use strict';

class Node {
    constructor(val, next=null) {
        this.val = val;
        this.next = next;
    }
}

class Stack {
    constructor() {
        this.top = null;
        this.length = 0;
    }

    push(val) {
        if (this.length === 0) {
            this.top = new Node(val)
            this.length++;
            return
        }

        this.top = new Node(val, this.top);
        this.length++;
    }

    pop() {
        if (this.length === 0) {
            throw new Error('Stack is empty');
        }
        let val = this.top.val;
        this.top = this.top.next;
        this.length--;
        return val
    }

    peek() {
        if (this.top) {
            return this.top.val
        } else {
            return null
        }
    }
}

module.exports = {Stack,
                  Node}