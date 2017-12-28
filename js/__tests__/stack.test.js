'use strict';

let stack = require('../stack');

test('Test that the push method adds values to stack.', () => {
    let s = new stack.Stack();
    s.push(1)
    s.push(2)
    expect(s.top.val).toBe(2)
    expect(s.top.next.val).toBe(1)
});

test('Test pop method pops correct val.', () => {
    let s = new stack.Stack();
    s.push(1)
    s.push(2)
    expect(s.pop()).toBe(2)
    expect(s.pop()).toBe(1)
    expect(() => s.pop()).toThrow()
});

test('Test pop method works one val in list', () => {
    let s = new stack.Stack()
    s.push(1)
    expect(s.pop()).toBe(1)
    expect(() => s.pop()).toThrow()
});

