'use strict';

let deque = require('../deque');

test('Test that length returns zero if nothing in list', () => {
    let d = new deque.Deque();
    expect(d.size()).toBe(0);
})