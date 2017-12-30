'use strict';

let bst = require('../bst');

test('Test root is null on init.', () => {
    let b = new bst.Bst();
    expect(b.root).toBeNull();
});