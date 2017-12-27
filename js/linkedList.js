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
            for (i = 0; i < length(iterable); i++) {
                self.push(iterable[i]);
            }
        }
    }



};

module.exports = {LinkedList,
                  Node};