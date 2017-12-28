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
        this._size = 0;
    }

    push(val) {
        if (this._size === 0) {
            this.top = new Node(val)
            this._size++;
            return
        }

        this.top = new Node(val, this.top);
        this._size++;
    }

    pop() {
        if (this._size === 0) {
            throw new Error('Stack is empty');

        }
        let val = this.top.val;
        this.top = this.top.next;
        this._size--;
        return val
    }

    peek() {

    }
}

module.exports = {Stack,
                  Node}