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


**Binary Heap**
A binary heap data structure is a tree type data structure that sorts the nodes relative to their parent/child relationship.

`def pop()`:  O(log n)

`def push(val)`:  O(log n)


**Priority Queue**
The priority queue data structure provides a way to represent data in a ordered "priority".  The benefit using this data structure has is that you can insert a new value at the given priority level without having to resort the entire list.  This makes adding new values much more efficient.  Our priority queue uses a high number = higher priority structure.

`def insert(val, priority)`: O(1)

`def pop()`:  O(n)

`def peek()`:  O(n)


**Unweighted Directed Graph**
A graph datastructure is an abstract way to represent data. Our graph uses a dictionary to store the node values and the edges are stored in a list for each node.

`nodes()`: O(n)

`edges()`: O(n^2)

`add_node(val)`: O(1)

`add_edge(val1, val2)`: O(1)

`del_node(val)`: O(n)

`del_edge(val1, val2)`: O(1)

`has_node(val)`: O(1)

`neighbors(val)`: O(1)

`adjacent(val1, val2)`: O(1)

`breadth_first_traversal(val)`: O(E + V) *

`depth_first_traversal(val)`: O(E + V) *

* where E is the number of edges and V is the number of Vertices via: https://stackoverflow.com/questions/6850357/explanation-of-runtimes-of-bfs-and-dfs


**Weighted Directed Graph**
A weighted graph is a graph that has weights assigned to the pointers.  A useful example of weighted pointers is how mapping software determines the distance between objects.  The objects are nodes, the weight in the pointers are the distances.

`nodes()`: O(n)

`edges()`: O(n * k)

`add_node(val)`: O(1)

`add_edge(val1, val2, weight)`: O(1)

`del_node(val)`: O(n)

`del_edge(val1, val2)`: O(1)

`has_node(val)`: O(1)

`neighbors(val)`: O(1)

`adjacent(val1, val2)`: O(1)

`breadth_first_traversal(val)`: O(n * k)

`depth_first_traversal(val)`: O(n * k)

###### Shortest Path Alogorithms:
`dijkstra(start, targe)`: O(E + VlogV)

`bellmanford(start, target)`:O(V * E)

The benefit of Dijkstra's shortest path algorithm is its efficiency and time complexity. However it does not report if the graph contains any negative looping paths.

The Bellmanford will alert the user of any negative cycles in the graph. However, this algorithm has a worse time complexity than Dijkstras.

**Unballanced Binary Search Tree**
A binary search tree is a node based data structure where the left subtree of a node contains values less than the node, and the right subtree contains values greater than the node.

`insert()`: O(n) Worst Case, O(log(n)) Average

`search()`: O(n) Worst Case, O(log(n)) Average

`size()`: O(1)

`depth()`: O(n) (recursive method)

`contains`: O(n) Worst Case, O(log(n)) Average

`balance`: O(n) (recursive method)

`delete`: O(log(n))


**Unballanced Binary Search Tree Traversal**
Moving through and returning values from a binary search tree (built with generators). 

Tree traversal example:
```
from bst import BinarySearchTree()

bst = BinarySearchTree()

bst_traversal = bst.in_order()

next(bst_traversal) # returns next number in traversal from generator 
```


`in_order()`: O(n)

`pre_order()`: O(n)

`post_order()`: O(n)

`breadth_first()`: O(n * k) / (Nodes * Edges)
