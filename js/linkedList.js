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
    }
};

module.exports = LinkedList;