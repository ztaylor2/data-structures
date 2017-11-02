"""
Priority Que that takes an optional priority value and returns the
value with the highest priority. The default priority is 0.
"""


class PriorityQue(object):
    """Priority Que that returns values based on priority."""

    def __init__(self):
        """Initialize the priority que, initializing a dictionary."""
        self.p_que = {}

    def insert(self, data, priority=0):
        """Insert value and an optional priority parameter."""
        if isinstance(data, (tuple, list)):
            for item in data:
                self.insert(item, priority)
        else:
            try:
                self.p_que[priority].append(data)
            except KeyError:
                self.p_que[priority] = [data]

    def peek(self):
        """Look at the next value that would be popped."""
        try:
            priority = sorted(self.p_que.keys(), reverse=True)
            return self.p_que[priority[0]][0]
        except IndexError:
            raise IndexError('Cannot peek empty queue.')

    def pop(self):
        """Remove the highest priority value and return it. If multiple
        values have the same priority it will return the value that
        was inserted first.
        """
        priority = sorted(self.p_que.keys(), reverse=True)
        try:
            return self.p_que[priority[0]].pop(0)
        except IndexError:
            try:
                self.p_que.pop(priority[0])
                return self.pop()
            except TypeError:
                raise IndexError('Cannot pop empty queue.')
