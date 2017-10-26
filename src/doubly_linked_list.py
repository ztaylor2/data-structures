# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:19:54 2017

@author: john_jensen
"""

class Node(object):
    """."""

    def __init__(self, data, next, previous):
        """."""
        self.data = data
        self.next = next
        self.previous = previous


class DoubleLinkedList(object):
    """."""

    def __init__(self):
        """."""
        self.head = None
        self.tail = None
        self._count = 0

    def push(self, data):
        """."""
        if self._count == 0:
            new_node = Node(data, None, None)
            self.head = new_node
            self.tail = new_node
            self._count += 1
        else:
            new_node = Node(data, self.head, None)
            self.head.previous = new_node
            self.head = new_node
            self._count += 1

    def append(self, data):
        """."""
        if self._count == 0:
            new_node = Node(data, None, None)
            self.head = new_node
            self.tail = new_node
            self._count += 1
        else:
            new_node = Node(data, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node
            self._count += 1

    def __len__(self):
        """."""
        return self._count

    def pop(self):
        """."""
        if not self.head:
            raise IndexError('The list is empty.')
        val_to_return = self.head.data
        self.head = self.head.next
        self.head.previous = None
        self._count -= 1
        return val_to_return

    def shift(self):
        """."""
        if not self.head:
            raise IndexError('The list is empty.')
        val_to_return = self.tail.data
        self.tail = self.tail.previous
        self.tail.next = None
        self._count -= 1
        return val_to_return

    def remove(self, val):
        """."""
        

