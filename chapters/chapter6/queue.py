from stack import Empty

class ArrayQueue:
    """ Array Implementation of a queue """
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """ Initialize list with empty values """
        self._data = [None] * self.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0
    
    def __len__(self):
        """ Returns the size of Queue"""
        return self._size
    
    def is_empty(self):
        """ Returns True if the queue is empty False otherwise """
        return self._size == 0
    
    def first(self):
        """ Returns the first element in the queue.
        Raises Empty exception if the queue is empty
        """

        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]
    
    def dequeue(self):
        """ Removes and returns the first element in the queue (FIFO) 
        Raises Empty exception if queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        front_val = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        # Reduce the size of the queue to half if 1/4 th of the list is free
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        
        return front_val
    
    def enqueue(self, item):
        """ Adds an item into the queue. 
        If the queue is full, we resize it to double the length 
        """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        index = (self._front + self._size) % len(self._data)
        self._data[index] = item
        self._size += 1

    def _resize(self, capacity):
        """Resizes the queue with the specified capacity
        """
        old_data = self._data

        self._data = [None] * capacity
        front = self._front

        for val in range(self._size):
            self._data[val] = old_data[front]
            front = (front + 1) % len(old_data)
        self._front = 0
    
    def __str__(self):
        return ','.join(str(item) for item in self._data)

if __name__ == "__main__":
    Q = ArrayQueue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    Q.enqueue(5)
    Q.enqueue(6)
    Q.enqueue(3)
    Q.enqueue(7)
    print("DELETING")
    print(Q.dequeue())
    print("FIRST ELEMENT: {}".format(Q.first()))
    Q.enqueue(19)
    Q.enqueue(34)
    Q.enqueue(67)
    Q.enqueue(45)
    Q.enqueue(45)
    print(Q)
    
    for _ in range(9):
        Q.dequeue()
    
    Q.enqueue(101)
    Q.enqueue(102)
    print(Q)
