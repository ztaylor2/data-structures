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
        if (this._length === 0) {
            return null
        }

        if (this._length === 1) {
            let popped_val = this.head.val;
            this.head = null;
            this._length--;
            return popped_val
        }

        let node = this.head;
        while (node.next.next) {
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
            if (node.val === val) {
                return node;
            }
            node = node.next;
        }
        return null;
    }

    remove(val) {
        if (this._length === 0) {
            throw new Error('List is empty.'); 
        }

        if (this.head.val === val) {
            this.head = this.head.next;
            this._length--;
            return
        }

        let node = this.head;
        while (node.next) {
            if (node.next.val === val) {
                node.next = node.next.next;
                this._length--;
                return;
            }
            node = node.next;
        }

        throw new Error('Value not in list');
    }

    display() {
        let output_string = '('
        let node = this.head;
        while (node) {
            if (typeof node.val === 'string' || node.val instanceof String)
                output_string += `\'${node.val}\', `
            else
                output_string += `${node.val}, `
            node = node.next;
        }
        output_string = output_string.slice(0, -2);
        return output_string += ')'
    }
};

module.exports = {LinkedList};