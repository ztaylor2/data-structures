'use strict';

class Node {
    constructor(val, left_child=null, right_child=null, parent=null) {
        this.val = val;
        this.left_child = left_child;
        this.right_child = right_child;
        this.parent = parent;
   }
}