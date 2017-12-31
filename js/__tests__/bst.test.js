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

test('Test insert adds values as expected', () => {
    let b = new bst.Bst();
    b.insert(5);
    b.insert(6);
    b.insert(7);
    b.insert(8);
    b.insert(4);
    b.insert(3);
    expect(b.root.right.right.right.val).toBe(8);
    expect(b.root.left.left.val).toBe(3);
    b.insert(3.5);
    expect(b.root.left.left.right.val).toBe(3.5)
});

test('Test search method returns root node', () => {
    let b = new bst.Bst();
    b.insert(1)
    expect(b.search(1)).toBe(b.root);
});

test('Test search method returns correct node', () => {
    let b = new bst.Bst();
    b.insert(5);
    b.insert(7);
    b.insert(6);
    expect(b.search(6)).toBe(b.root.right.left);
});

test('Test size method returns correct size when empty', () => {
    let b = new bst.Bst();
    expect(b.size()).toBe(0);
});

test('Test size method returns after inserting', () => {
    let b = new bst.Bst();
    b.insert(1);
    b.insert(2);
    b.insert(3);
    expect(b.size()).toBe(3)
});

test('Test contains method returns true', () => {
    let b = new bst.Bst();
    b.insert(1);
    expect(b.contains(1)).toBe(true);
});

test('Test contains method returns false', () => {
    let b = new bst.Bst();
    expect(b.contains(1)).toBe(false);
});

test('Test contains method returns true full tree', () => {
    let b = new bst.Bst();
    b.insert(1);
    b.insert(2);
    b.insert(3);
    b.insert(4);
    b.insert(3.5);
    expect(b.contains(3.5)).toBe(true);
});

test('Test bubble up depths', () => {
    let b = new bst.Bst();
    b.insert(2);
    b.insert(1);
    b.insert(3);
    expect(b.root.depth).toBe(2);
})