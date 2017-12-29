'use strict';

let deque = require('../deque');

test('Test that length returns zero if nothing in list', () => {
    let d = new deque.Deque();
    expect(d.size()).toBe(0);
});

test('Test pop and popleft methods return null if empty.', () => {
    let d = new deque.Deque();
    expect(d.peek()).toBeNull();
    expect(d.peekleft()).toBeNull();
});

test('Test append adds value to right of deque and peek.', () => {
    let d = new deque.Deque();
    d.append(1)
    d.append(2)
    expect(d.peek()).toBe(2)
});

test('Test appendleft adds values to left of deque and peekleft.', () => {
    let d = new deque.Deque();
    d.appendleft(1)
    d.appendleft(2)
    expect(d.peekleft()).toBe(2)
});

// test('Test ')