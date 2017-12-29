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
        if (this.length === 0) {
            throw new Error('List is empty.')
        } else if (this.length === 1) {
            let val = this.tail.val;
            this.head = null;
            this.tail = null;
            this.length--;
            return val
        } else {
            let val = this.tail.val;
            this.tail = this.tail.prev;
            this.tail.next = null;
            this.length--;
            return val
        }

    }

    shift() {
        if (this.length === 0) {
            throw new Error('List is empty.')
        } else if (this.length === 1) {
            let val = this.head.val;
            this.head = null;
            this.tail = null;
            this.length--;
            return val
        } else {
            let val = this.head.val;
            this.head = this.head.next;
            this.head.prev = null;
            this.length--;
            return val
        }
    }

    remove(val) {
        if (this.head.val === val) {
            this.shift()
        } else if (this.tail.val === val) {
            this.pop()
        } else {
            let node = this.head;
            while (node) {
                if (node.val === val) {
                    node.prev.next = node.next;
                    node.next.prev = node.prev;
                    self.length--;
                    return
                }
                node = node.next;
            }
        }
    }
}

module.exports = {Dll}