"""
Math 560
Project 2
Fall 2020

p2queue.py

Partner 1: William He
Partner 2: Zihao Lin
Date: 10/15/2020
"""

"""
Queue Class
"""
class Queue:

   """
   Class attributes:
   queue    # The array for the queue.
   front    # The index of the front of the queue.
   rear     # The index ONE PAST the rear of the queue.
   numElems # The number of elements in the queue.
   """

   """
   __init__ function to initialize the Queue.
   Note: intially the size of the queue defaults to 3.
   Note: the queue is initally filled with None values.
   """
   def __init__(self, size=3):
       self.queue = [None for x in range(0,size)]
       self.front = 0
       self.rear = 0
       self.numElems = 0
       return

   """
   __repr__ function to print the stack.
   """
   def __repr__(self):
       s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
       s += ('Front: %d' % self.front) + '\n'
       s += ('Rear: %d' % self.rear) + '\n'
       s += ('numElems: %d' % self.numElems) + '\n'
       return s

   """
   isFull function to check if the queue is full.
   Input: queue
    Output: boolean if queue is full
   """
   def isFull(self):

       return self.rear >= len(self.queue)

   """
   isEmpty function to check if the queue is empty.
   Input: queue
    Output: boolean if queue has no elements
   """
   def isEmpty(self):
       return self.numElems<=0

   """
   resize function to resize the queue by doubling its size.
   Note: we also reset the front to index 0.
   Input: queue
   Output: queue with size doubled 
   """
   def resize(self):

       newQueue = [None for x in range(0, 2*len(self.queue))]
       for i in range(0, self.numElems):
           newQueue[i] = self.queue[self.front+i]
       self.queue = newQueue.copy()
       self.rear=self.rear-self.front
       self.front=0

       return

   """
   push function to push a value into the rear of the queue.
   Input: queue and value
   Output: queue (resized if needed) with value pushed
   """
   def push(self, val):

       if self.isFull():
           self.resize()
       self.queue[self.rear] = val
       self.rear = self.rear + 1
       self.numElems = self.numElems + 1

       return

   """
   pop function to pop the value from the front of the queue.
   Input: Queue
   Output: least recently pushed element returned and removed from queue
   """
   def pop(self):

       if self.isEmpty():
           return None
       element = self.queue[self.front]
       self.queue[self.front] = None
       self.front = self.front + 1
       self.numElems = self.numElems - 1

       return element
