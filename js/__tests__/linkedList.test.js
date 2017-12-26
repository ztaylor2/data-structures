let linkedList = require('../linkedList');

test('Test that head is null on initialization', () => {
    let ll = new linkedList.LinkedList();
  expect(ll.head.toBe(null));
});