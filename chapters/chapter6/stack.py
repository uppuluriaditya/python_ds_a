class Empty(Exception):
    """ Class to raise an exception if the stack is empty """
    pass

class ArrayStack:
    """ Stack implementation using list data strcture """

    def __init__(self):
        """ Iniitialize a list """
        self._data = []
    
    def push(self, item):
        """ Pushes the item into the list """
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

if __name__ == "__main__":
    stack = ArrayStack()
    stack.push(5)
    stack.push(9)
    print(len(stack))
    stack.pop()
    stack.pop()
    try:
        stack.pop()
    except Empty as err:
        print(err)

    stack.push(5)
    stack.push(9)
    print(stack.top())
    
