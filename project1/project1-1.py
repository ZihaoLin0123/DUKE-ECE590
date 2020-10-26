"""
Math 560
Project 1
Fall 2020

Partner 1: Xueyang Liu
Partner 2: Han Gong 
Date: 10/4/2020
"""

"""
SelectionSort
"""
def SelectionSort(listToSort):
    n = len(listToSort)
    for i in range(0, n):
        min_idx = i
        for j in range(i+1, n):
            if listToSort[j] < listToSort[min_idx]:
                min_idx = j
        listToSort[min_idx], listToSort[i]  = listToSort[i], listToSort[min_idx]

    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    n = len(listToSort)
    for i in range(1, n):
        current = listToSort[i]
        j = i - 1
        while j > -1:
            if current < listToSort[j]:
                listToSort[j+1] = listToSort[j]
                j -= 1
            else:
                break
        listToSort[j + 1] = current

    return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):
    n = len(listToSort)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if listToSort[j] > listToSort [j+1]:
                smaller = listToSort [j+1]
                listToSort[j+1] = listToSort[j]
                listToSort[j] = smaller

    return listToSort

"""
MergeSort
"""
def MergeSort(listToSort):

    if(len(listToSort)) == 0 or len(listToSort) == 1:
        return listToSort
    elif(len(listToSort) == 2):
        if(listToSort[0] > listToSort[1]):
            listToSort[0], listToSort[1] = listToSort[1], listToSort[0]
    else:
        divider = len(listToSort)//2
        a = MergeSort(listToSort[:divider])
        b = MergeSort(listToSort[divider:])

        i = 0
        j = 0
        k = 0

        while i < len(a) and j < len(b):
            if b[j] < a[i]:
                listToSort[k] = b[j]
                j += 1
                k += 1
            else:
                listToSort[k] = a[i]
                i += 1
                k += 1
        if i < len(a):
            listToSort[k:] = a[i:]
        if j < len(b):
            listToSort[k:] = b[j:]
    
    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    if j == None:
        j = len(listToSort)
    # Set default value for j if None.

    if j - i == 1 or j - i == 0:
        return listToSort
    # Base case for the recursion.
        
    if j - i > 1:
        l, r = i, j-1
        p = listToSort[(r-l)//2 + l]
        
        while l <= r:
            while r >= l and listToSort[l] < p: 
                l += 1
            while r >= l and listToSort[r] > p: 
                r -= 1             
            if l <= r:
                listToSort[l], listToSort[r] = listToSort[r], listToSort[l]
                l += 1
                r -= 1
            
        QuickSort(listToSort, i, r+1)
        QuickSort(listToSort, l, j)

    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('DEFAULT measureTime')
    print()
    measureTime(preSorted = False, numTrials = 30)
    
