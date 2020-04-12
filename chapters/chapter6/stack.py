class Empty(Exception):
    """ Class to raise an exception if the stack is empty """
    pass

class ArrayStack:
    """ Stack implementation using list data strcture """

    def __init__(self, capacity=10):
        """ Iniitialize a list """
        self._data = []
        self._capacity = capacity
    
    def push(self, item):
        """ Pushes the item into the list """
        if self.__len__() == self._capacity:
            self.pop()
        self._data.append(item)
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        """ Checks whether the current stack is empty """ 
        return len(self._data) == 0
    
    def top(self):
        """ Returns the element at the top of the stack. It will not remove the element
        Raises Empty Exception if stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]
    
    def pop(self):
        """ Removes and returns the element from the top of the stack
        Raises Empty exception is the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()
    
    def __str__(self):
        """ Shows the number of elements in the stack """
        return ','.join(str(item) for item in self._data)

if __name__ == "__main__":
    stack = ArrayStack(3)

    stack.push(5)
    stack.push(9)
    stack.push(10)
    stack.push(11)
    print(stack)
    
