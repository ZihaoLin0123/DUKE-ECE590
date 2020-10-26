"""
Math 560
Project 2
Fall 2020

project2.py

Partner 1: William He
Partner 2: Zihao Lin
Date: 10/15/20
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The shortest path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')
    #Reset maze prevs and visited booleans
    for i in range(len(maze.adjList)):
        maze.adjList[i].visited=False
        maze.adjList[i].prev=None
    if (alg=='BFS'):
        #Initialize queue and push start into queue.
        path = []
        queue = Queue()
        current = maze.start
        current.visited = True
        current.distance = 0
        queue.push(current.rank)
        #BFS starting from start vertex
        while not queue.isEmpty():
            #If there are elements to be processed, move to least recently pushed
            current = queue.pop()
            currVertex = maze.adjList[current]
            currVertex.visited = True
            for j in range(len(maze.adjMat[currVertex.rank])):
                #Identify neighbors of current vertex and mark as visited
                if maze.adjMat[currVertex.rank][j] == 1 and \
                        maze.adjList[j].visited==False:
                    maze.adjList[j].prev = currVertex
                    # If we are at exit, find pathway by backtracking using
                    # prevs
                    if maze.adjList[j].isEqual(maze.exit):
                        backtrack = maze.adjList[j]
                        path.insert(0, backtrack.rank)
                        while True:
                            path.insert(0, backtrack.prev.rank)
                            temp = backtrack.prev
                            backtrack = temp
                            if backtrack.prev.isEqual(maze.start):
                                path.insert(0, maze.start.rank)
                                break
                        break
                    #Push neighbor
                    queue.push(j)
        return path
    #Initialize stack and move to the start vertex
    path = []
    stack = Stack()
    current = maze.start
    current.visited = True
    current.distance = 0
    stack.push(current.rank)

    #Visit neighbors of to-be processed vertices
    while not stack.isEmpty():
        current = stack.pop()
        currVertex=maze.adjList[current]
        currVertex.visited=True
        for j in range(len(maze.adjMat[currVertex.rank])):
            #Identify neighbors of current vertex
            if maze.adjMat[currVertex.rank][j] == 1 and\
                    not maze.adjList[j].visited:
                maze.adjList[j].prev = currVertex
                #If we are at exit vertex, then backtrack using
                #prevs to determine path
                if maze.adjList[j].isEqual(maze.exit):
                    backtrack = maze.adjList[j]
                    path.insert(0, backtrack.rank)
                    while True:
                        path.insert(0, backtrack.prev.rank)
                        temp = backtrack.prev
                        backtrack = temp
                        if backtrack.prev.isEqual(maze.start):
                            path.insert(0,maze.start.rank)
                            break
                    break
                #Push neighbor
                stack.push(j)
    return path

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)