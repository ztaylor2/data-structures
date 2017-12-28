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

test('Test peek returns correct val.', () => {
    let s = new stack.Stack();
    s.push(1)
    s.push(2)
    s.push(3)
    expect(s.peek()).toBe(3)
});

test('Test push, pop, then peek.', () => {
    let s = new stack.Stack();
    s.push(1)
    s.push(2)
    s.push(3)
    expect(s.pop()).toBe(3)
    expect(s.peek()).toBe(2)
    expect(s.pop()).toBe(2)
    expect(s.peek()).toBe(1)
    expect(s.pop()).toBe(1)
    expect(s.peek()).toBeNull()
    expect(() => s.pop()).toThrow()
});

test('Test length returns correctly.', () => {
    let s = new stack.Stack();
    s.push(1)
    expect(s.length).toBe(1)
    s.push(2)
    expect(s.length).toBe(2)
    s.pop()
    expect(s.length).toBe(1)
    s.pop()
    expect(s.length).toBe(0)
})