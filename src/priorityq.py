"""."""


class P_Heap(object):
    """."""

    def __init__(self):
        """."""
        self.p_heap = {}

    def insert(self, data, priority=0):
        """.""" 
        if isinstance(data,(tuple, list)):
            for item in data:
                self.insert(item, priority)
        else:
            try:
                self.p_heap[priority].append(data)
            except KeyError:
                self.p_heap[priority] = [data]

    def peek(self):
        """."""
        try:
            priority = sorted(self.p_heap.keys(), reverse=True)
            return self.p_heap[priority[0][0]]
        except IndexError:
            raise 'Priority queue is empty'
        
    def pop(self):
        """."""
        try:    
            priority = sorted(self.p_heap.keys(), reverse=True)              
            return self.p_heap[priority[0]].pop(0)
        except IndexError:
            raise 'Priority queue is empty'
        except TypeError:
            pass
            # TODO delete the key and re call pop()
