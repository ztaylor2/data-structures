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

        this.head = new Node(val, head.next);
        this._size++;
    }

    pop() {

    }

    peek() {

    }
}

