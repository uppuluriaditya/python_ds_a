""" All common utilities live here"""

class Empty(Exception):
    """ Class to raise an exception if the stack is empty """
    pass

class Full(Exception):
    """ Class to raise an exception if the stack is full """