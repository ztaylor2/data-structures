# Data-Structures
**Classic data structures in python.  Paired programming.**

**Authors: Zach Taylor & John Jensen**

**Linked List**
Linked list is a linked data structure with only one pointer to the next node.

`def push(self, data):` O(1)

`def pop(self):` O(1)

`def size(self):` O(1)

`def search(self, val):` O(n)

`def display(self):` O(n)

`def __len__(self):` O(1)

`def remove(self, node):` O(n)

`def __str__(self):` O(1)

**Stack**
A stack is a data structure where elements are stacked on top of one another. It operates in a first in first out fashion.

`def __len__(self):` O(1)

`def push(self, value):` O(1); unless pushed with iterable, then O(n)

`def pop(self):` 

**Doubly Linked List**
Doubly linked list is a linked data structure that has a link to previous and next nodes from inside of it.

Time Complexity:

`def __len__(self):` O(1)

`def push(self, val):` O(1); unless initiated with iterable, then O(n)

`def append(self, val):` O(1)

`def pop(self):` O(1)

`def shift(self):` (1)

`def remove(self, val):` O(n)


**Queue**
We used composition from our doubly linked list to build our queue. The queue adds(enqueues) elements on one end and removes (dequeues) from the other end.

Time Complexity:

`def enqueue(self):` O(1); unless initiated with iterable, then O(n)

`def dequeue(self):` O(1)

`def peek(self):` O(1)

`def __len__(self):` O(1); count changes as enqueued and dequeued


**Deque**
The deque is a data structure that allows data to be inserted and removed from each end.

Time Complexity:

`def append(val):`  0(1)

`def appedleft(val):`  O(1)

`def pop()`:  O(1)

`def popleft()`:  O(1)

`def peek()`:  O(1)

`def peekleft()`:  O(1)

`def size()`:  O(1)