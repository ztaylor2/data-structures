'use strict';

class Node {
    constructor(val, left=null, right=null, parent=null) {
        this.val = val;
        this.left = left;
        this.right = right;
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
            this._size++;
            return;
        }

        let current_node = self.root
        while (current_node) {
            if (val > current_node.val) {
                if (current_node.right) {
                    current_node = current_node.right;
                    continue;
                } else {
                    current_node.right = new Node(val, null, null, current_node);
                    this._size++;
                    return;
                }
            } else if (val < current_node.val) {
                if (current_node.left) {
                    current_node = current_node.left;
                    continue;
                } else {
                    current_node.left = new Node(val, null, null, current_node);
                    this._size++;
                    return;
                }
            }
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