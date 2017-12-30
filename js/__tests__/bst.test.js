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