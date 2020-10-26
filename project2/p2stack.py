"""
Math 560
Project 2
Fall 2020

p2stack.py

Partner 1: William He
Partner 2: Zihao Lin
Date: 10/15/20
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: initially the size of the stack defaults to 3.
    Note: the stack is initially filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=3):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.stack)) + ' ]\n'
        s += ('Top: %d' % self.top) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the stack is full.
    Input: stack
    Output: boolean if stack is full
    """
    def isFull(self):
        return self.top >= len(self.stack)-1

    """
    isEmpty function to check if the stack is empty.
    Input: stack
    Output: boolean if stack has no elements
    """
    def isEmpty(self):
        return self.numElems<=0

    """
    resize function to resize the stack by doubling its size.
    Input: stack
    Output: stack with size doubled
    """
    def resize(self):
        newStack=[None for x in range(0,2*len(self.stack))]
        for i in range(0,len(self.stack)):
            newStack[i]=self.stack[i]
        self.stack=newStack.copy()
        return

    """
    push function to push a value onto the stack.
    Input: stack attribute, value
    Output: stack attribute with value pushed
    """
    def push(self, val):
        if self.isFull():
            self.resize()
        self.stack[self.top+1]=val
        self.numElems=self.numElems+1
        self.top=self.top+1
        return

    """
    pop function to pop the value off the top of the stack.
    Input: stack
    Output: most recently pushed element returned and removed
    """
    def pop(self):
        if self.isEmpty():
            return None
        element=self.stack[self.top]
        self.stack[self.top]=None
        self.top=self.top-1
        self.numElems=self.numElems-1
        return element