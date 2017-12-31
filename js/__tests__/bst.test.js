'use strict';

let bst = require('../bst');

test('Test root is null on init.', () => {
    let b = new bst.Bst();
    expect(b.root).toBeNull();
});

test('Test insert when empty', () => {
    let b = new bst.Bst();
    b.insert(1);
    expect(b.root.val).toBe(1);
});

test('Test insert a couple values.', () => {
    let b = new bst.Bst();
    b.insert(2);
    b.insert(1);
    b.insert(3);
    expect(b.root.val).toBe(2);
    expect(b.root.right.val).toBe(3);
    expect(b.root.left.val).toBe(1);
});