let linkedList = require('../linkedList');

test('Test that head is null on initialization', () => {
    let ll = new linkedList.LinkedList();
    expect(ll.head).toBeNull();
});

test('Test push inserts vals and increases length', () => {
    let ll = new linkedList.LinkedList();
    ll.push(2)
    ll.push(1)
    expect(ll.head.val).toBe(1)
    expect(ll.head.next.val).toBe(2)
    expect(ll.head.next.next).toBeNull()
});

test('Test init with iterable.', () => {
    let ll = new linkedList.LinkedList([2, 1]);
    expect(ll.head.val).toBe(1)
    expect(ll.head.next.val).toBe(2)
    expect(ll.head.next.next).toBeNull()
});

test('Test pop returns correct value.', () => {
    let ll = new linkedList.LinkedList([2, 1]);
    expect(ll.pop()).toBe(2)
    expect(ll.head.next).toBeNull()
});

test('Test counter workes after push and pop', () => {
    let ll = new linkedList.LinkedList([1, 2, 3, 4, 5]);
    ll.pop()
    ll.pop()
    expect(ll.size()).toBe(3)
})