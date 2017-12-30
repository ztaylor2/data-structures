'use strict';

class Node {
    constructor(val, left_child=null, right_child=null, parent=null) {
        this.val = val;
        this.left_child = left_child;
        this.right_child = right_child;
        this.parent = parent;
   }
}

class Bst {
    constructor() {
        this.root = null;
        this._size = 0
    }

    insert(val) {
        if (this._size === 0) {
            this.root = new Node(val);
        }
    }

    search(val) {

    }

    size() {
        return this._size;
    }

    depth() {

    }

    contains() {

    }

    balance() {

    }

}

module.exports = {Bst}