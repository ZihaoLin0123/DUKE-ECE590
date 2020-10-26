"""
Math 560
Project 3
Fall 2020

Partner 1: William He wrh23
Partner 2: Zihao Lin zl293
Date: Oct. 25 2020
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""

def detectArbitrage(adjList, adjMat, tol=1e-15):
    ##### Your implementation goes here. #####

    # initialize some characteristics of vertex
    for vertex in adjList:
        vertex.dist = math.inf
        vertex.prev = None

    # initialize a start vertex
    start = adjList[0]
    start.dist = 0

    # iterate |V|-1 times, normal Bellman-Ford
    for iter in range(0, len(adjMat) - 1):
        for u in adjList:
            for v in u.neigh:
                if v.dist > u.dist + adjMat[u.rank][v.rank] + tol:
                    v.dist = u.dist + adjMat[u.rank][v.rank]
                    v.prev = u

    # Extra iteration while tracking distances
    dists = [0 for x in range(0,len(adjMat)-1)]
    for i in range(0, len(adjMat)-1):
        dists[i] = adjList[i].dist

    # update the distance to check which vertexes' distances decreased
    for u in adjList:
        for v in u.neigh:
            if v.dist > u.dist + adjMat[u.rank][v.rank] + tol:
                v.dist = u.dist + adjMat[u.rank][v.rank]
                v.prev = u

    # initialize a decreased vertex
    decreasedVertex = None

    # check which vertexes' distances decreased
    for i in range(0, len(adjMat)-1):
        if adjList[i].dist < dists[i]:
            decreasedVertex = adjList[i]
            break

    # if no such vertex, return an empty list
    if decreasedVertex == None:
        return []

    # else
    # first initialize negative cycle whose start vertex is the decreased vertex
    negCycle = [decreasedVertex.prev.rank]  # the list of rank of each vertex in the path of negative cycle

    currVertex = adjList[negCycle[0]]  # current vertex is the start of the negative cycle
    currVertex = currVertex.prev.rank  # move the current vertex to the previous one

    # find the negative cycle path
    while not adjList[currVertex].isEqual(adjList[negCycle[0]]):
        negCycle.append(currVertex)
        currVertex = adjList[currVertex].prev.rank
    negCycle.append(negCycle[0])
    negCycle.reverse()
    return negCycle

################################################################################

"""
rates2mat
"""
def rates2mat(rates):

    # Currently this only returns a copy of the rates matrix.

    return [[-math.log(R) for R in row] for row in rates]


"""
Main function.
"""
if __name__ == "__main__":
    testRates()
