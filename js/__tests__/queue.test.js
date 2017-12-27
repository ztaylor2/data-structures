'use strict';

let queue = require('../queue');

test('Test enqueue adds values.', () => {
    let q = new queue.Queue();
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    expect(q.head.val).toBe(3)
    expect(q.head.next.val).toBe(2)
    expect(q.head.next.next.val).toBe(1)
    expect(q.head.next.next.next).toBeNull()
});

test('Test size returns size after enqueing vals.', () => {
    let q = new queue.Queue();
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    expect(q.size()).toBe(3)
});

test('Test peek returns correct value.', () => {
    let q = new queue.Queue();
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    expect(q.peek()).toBe(1)
});

test('Test dequeue list length one.', () => {
    let q = new queue.Queue();
    q.enqueue(1)
    expect(q.dequeue()).toBe(1)
})

test('Test dequeue list length greater than one', () => {
    let q = new queue.Queue();
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    expect(q.dequeue()).toBe(1)
})