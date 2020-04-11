import ctypes

class DynamicArray:
    """ A Dynamic Array class relatively equal to python list 
    Three things to consider here:
        * _n The number of actual elements currently stored in the list
        * _capacity The maximum number of elements that could be stored in the 
                currently allocated array
        * _A The reference to the currently allocated array (initially None)
    """

    def __init__(self):
        """ Create an Empty Array """
        self._len = 0
        self._capacity = 1
        self._array = self._make_array(self._capacity)
    
    def __len__(self):
        """ Returns the number of elements stored in the array """
        return self._len

    def __get_item__(self, index):
        """ Returns the item at the specified at index . Raises error otherwise """
        if not 0 <= index < self._len:
            raise IndexError('invalid index {}'.format(index))
        return self._array[index]

    def append(self, item):
        """ Adds the object to the end of array """
        if self._len == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._len] = item
        self._len += 1
    
    def insert(self, index, item):
        """ Inserts the item at the specified index """
        if self._len == self._capacity:
            self._resize(2 * self._capacity)

        for j in range(self._len, index, -1):
            self._array[j] = self._array[j-1]

        self._array[index] = item
        self._len += 1

    def remove(self, value):
        """ Removes the first occurance of a value. Raises ValueError otherwise """
        for k in range(self._len):
            if self._array[k] == value:
                for j in range(k, self._len - 1):
                    self._array[j] = self._array[j+1]
                self._array[self._len - 1] = None
                self._len -= 1
                return
        raise ValueError("Value not found")

    def _resize(self, capacity):
        """ Resizes the array to the specified capacity """
        B = self._make_array(capacity)
        for k in range(self._len):
            B[k] = self._array[k]
        self._array = B
        self._capacity = capacity

    def _make_array(self, capacity):
        """ Returns a new array of specified capacity """
        return (capacity * ctypes.py_object)()
    
    def __str__(self):
        return '[' + ','.join([str(self._array[i]) for i in range(self._len)]) + ']'

if __name__ == "__main__":
    a = DynamicArray()
    a.append(4)
    a.append(5)
    a.append(6)
    print(a)
    a.insert(2, 7)
    print(a)

    a.remove(5)
    print(a)