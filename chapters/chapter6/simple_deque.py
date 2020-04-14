from stack import Empty

class ArrayDeque:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        """ Returns the number of elements """
        return len(self._data)

    def is_empty(self):
        """ Returns True if empty"""
        return len(self._data) == 0

    def add_first(self, item):
        """ Add element to the front of the deque """
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = item
        self._size += 1

    def add_last(self, item):
        """ Add element to the back of the deque """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        index = (self._front + self._size) % len(self._data)
        self._data[index] = item
        self._size += 1

    def delete_first(self):
        """ Removes and returns the element from the front of the deque
        Raises Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Empty("Deque is Empty")
        front_val = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        # Reduce the size of the queue to half if 1/4 th of the list is free
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        
        return front_val

    def delete_last(self):
        """ Removes and returns the element from the back of the deque 
        Raises Empty exception id the deque is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        back = (self._front - 1 + self._size) % len(self._data)
        val = self._data[back]
        self._data[back] = None
        self._size -= 1
        
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        
        return val

    def first(self):
        """ Returns the first element of the deque. 
        Raises Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Empty("deque is empty")
        return self._data[self._front]

    def last(self):
        """ Returns the last element of the deque
        Raises Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Empty("deque is empty")
        back = (self._front - 1 + self._size) % len(self._data)
        return self._data[back]

    def _resize(self, capacity):
        """ Resizes the deque with the specified capacity """
        old_data = self._data

        self._data = [None] * capacity
        front = self._front

        for val in range(self._size):
            self._data[val] = old_data[front]
            front = (front + 1) % len(old_data)
        self._front = 0


if __name__ == "__main__":
    D = ArrayDeque()
    for i in range(5):
        D.add_last(i+1)
    
    assert D.last() == 5
    assert D.first() == 1

    assert D.delete_first() == 1
    assert D.delete_last() == 5

    D.add_last(11)
    assert D.last() == 11
    assert D.first() == 2

    D.add_first(12)
    assert D.first() == 12

    assert D.first() == 12

    assert D.last() == 11
    assert D.delete_first() == 12
    assert D.delete_last() == 11

    assert D.first() == 2