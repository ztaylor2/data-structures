'use strict';

class Node {
    constructor(val, next=null, prev=null) {
        this.val = val;
        this.next = next;
        this.prev = prev;
    }
}

class Deque {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    append(val) {

    }

    appendleft(val) {

    }

    pop() {

    }

    popleft() {

    }

    peek() {
        if (this.length === 0) {
            return null
        }
        return this.tail.val
    }

    peekleft() {
        if (this.length === 0) {
            return null
        }
        return this.head.val
    }

    size() {
        return this.length
    }
}

module.exports = {Deque}