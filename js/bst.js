'use strict';

class Node {
    constructor(val, left=null, right=null, parent=null, depth=1) {
        this.val = val;
        this.left = left;
        this.right = right;
        this.parent = parent;
        this.depth = depth;
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

        let current_node = this.root
        while (current_node) {
            if (val > current_node.val) {
                if (current_node.right) {
                    current_node = current_node.right;
                    continue;
                } else {
                    current_node.right = new Node(val, null, null, current_node);
                    this._bubble_up_depths(current_node.right);
                    this._size++;
                    return;
                }
            } else if (val < current_node.val) {
                if (current_node.left) {
                    current_node = current_node.left;
                    continue;
                } else {
                    current_node.left = new Node(val, null, null, current_node);
                    this._bubble_up_depths(current_node.left);
                    this._size++;
                    return;
                }
            }
        }
    }

    _bubble_up_depths(node) {
        let current_node = node;
        while (current_node.parent) {
            if (current_node.parent.depth <= current_node.depth) {
                current_node.parent.depth = current_node.depth + 1;
            }
            current_node = current_node.parent;
        }
    }

    search(val) {
        if (!this.root) {
            return null;
        }

        let current_node = this.root;
        while (current_node) {
            if (val === current_node.val) {
                return current_node;
            } else if (val < current_node.val) {
                current_node = current_node.left;
            } else if (val > current_node.val) {
                current_node = current_node.right;
            }
        }

        return null;
    }

    size() {
        return this._size;
    }

    depth() {
        return this.root.depth;
    }

    contains(val) {
        if (this.search(val)) {
            return true;
        } else {
            return false;
        }
    }

    balance() {
        return this.root.right.depth - this.root.left.depth
    }

}

module.exports = {Bst}