'use strict';

let dll = require('../dll');

test('Test push method adds one val correctly.', () => {
    let d = new dll.Dll();
    d.push(1)
    expect(d.head.val).toBe(1)
    expect(d.head.next).toBeNull()
    expect(d.head.prev).toBeNull()
    expect(d.tail.val).toBe(1)
    expect(d.tail.next).toBeNull()
    expect(d.tail.prev).toBeNull()
});

test('Test push two vals into list.', () => {
    let d = new dll.Dll();
    d.push(1)
    d.push(2)
    expect(d.head.val).toBe(2)
    expect(d.head.next).toBe(d.tail)
    expect(d.head.prev).toBeNull()
    expect(d.tail.val).toBe(1)
    expect(d.tail.prev).toBe(d.head)
    expect(d.tail.next).toBeNull()
});

test('Test push three values into list.', () => {
    let d = new dll.Dll();
    d.push(1)
    d.push(2)
    d.push(3)
    expect(d.head.val).toBe(3)
    expect(d.head.prev).toBeNull()
    expect(d.head.next.val).toBe(2)
    expect(d.head.next.next.val).toBe(1)
    expect(d.tail.next).toBeNull()
    expect(d.tail.prev.val).toBe(2)
    expect(d.tail.prev.prev.val).toBe(3)
});

test('Test append one value.', () => {
    let d = new dll.Dll();
    d.append(1)
    expect(d.head.val).toBe(1)
    expect(d.tail.val).toBe(1)
    expect(d.head).toBe(d.tail)
    expect(d.head.next).toBeNull()
    expect(d.head.prev).toBeNull()
    expect(d.tail.next).toBeNull()
    expect(d.tail.prev).toBeNull()
});

test('Test append two values.', () => {
    let d = new dll.Dll();
    d.append(1)
    d.append(2)
    expect(d.tail.val).toBe(2)
    expect(d.head.val).toBe(1)
    expect(d.tail.prev).toBe(d.head)
    expect(d.head.next).toBe(d.tail)
    expect(d.tail.next).toBeNull()
    expect(d.head.prev).toBeNull()
});

test('Test append three values into list.', () => {
    let d = new dll.Dll();
    d.append(1)
    d.append(2)
    d.append(3)
    expect(d.tail.val).toBe(3)
    expect(d.head.val).toBe(1)
    expect(d.head.next).toBe(d.tail.prev)
    expect(d.head.next.val).toBe(2)
    expect(d.tail.next).toBeNull()
    expect(d.head.prev).toBeNull()
    expect(d.head.next.next).toBe(d.tail)
    expect(d.head.next.prev).toBe(d.head)
});