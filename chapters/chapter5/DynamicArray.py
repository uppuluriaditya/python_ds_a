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
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    
    def __len__(self):
        """ Returns the number of elements stored in the array """
        return self._n

    def __get_item__(self, index):
        """ Returns the item at the specified at index . Raises error otherwise """
        if not 0 <= index < self._n:
            raise IndexError('invalid index')
        return self._A[index]

    def append(self, item):
        """ Adds the object to the end of array """
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = item
        self._n += 1
    
    def _resize(self, capacity):
        """ Resizes the array to the specified capacity """
        B = self._make_array(capacity)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = capacity

    def _make_array(self, capacity):
        """ Returns a new array of specified capacity """
        return (capacity * ctypes.py_object)()

if __name__ == "__main__":
    a = DynamicArray()
    a.append(4)
    a.append(5)