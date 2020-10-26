"""
Math 560
Project 1
Fall 2020

Sorting

Partner 1: Zihao Lin, NetID: zl293
Date: Oct. 8th, 2020
"""

"""
1. SelectionSort
The function is an implementation of selection sorting algorithm.
The function could sort an input list of numbers and return it.
Its input is a list of numbers. 
It will sort the list and return itself in an increasing order.
"""


def SelectionSort(listToSort):

    # Iterate through the index of the list
    for i in range(len(listToSort)):

        # select the minimum from i-th number to the end number
        min_index = i
        for j in range(i+1, len(listToSort)):
            if listToSort[min_index] > listToSort[j]:
                min_index = j
                pass
            pass

        # after find the index of the minimum number,
        # we exchange the current number and the minimum number.
        listToSort[i], listToSort[min_index] \
            = listToSort[min_index], listToSort[i]

    return listToSort


"""
2. InsertionSort
The function is an implementation of insertion sorting algorithm.
The function could sort an input list of numbers and return it.
Its input is a list of numbers. 
It will sort the list and return itself in an increasing order.
"""


def InsertionSort(listToSort):

    # Iterate through the index of the list
    for k in range(1, len(listToSort)):

        # set the current value
        current_value = listToSort[k]

        # Iterate through from 0 to k.
        # If the (k-1-i)th number is larger than the current value,
        # insert the current value into the (k-1-i)th position,
        # and shift the (k-1-i)th value to the (k-i)th position.

        i = k - 1
        while i >= 0:
            if current_value < listToSort[i]:
                listToSort[i + 1] = listToSort[i]
                i -= 1
                pass
            else:
                break
            pass

        listToSort[i + 1] = current_value

    return listToSort


"""
3. BubbleSort
The function is an implementation of bubble sorting algorithm.
The function could sort an input list of numbers and return it.
Its input is a list of numbers. 
It will sort the list and return itself in an increasing order.
"""


def BubbleSort(listToSort):

    # first set change is true, which is a boolean variable used in loop
    change = True

    # iterate through the list and compare adjacent values
    # if they are our of order, swap them
    # repeat until no more swaps are made
    while change:
        change = False
        for i in range(len(listToSort)-1):
            if listToSort[i] > listToSort[i+1]:
                listToSort[i], listToSort[i+1] = listToSort[i+1], listToSort[i]
                change = True
    return listToSort


"""
4. MergeSort
The function is an implementation of bubble sorting algorithm.
The function could sort an input list of numbers and return it.
Its input is a list of numbers. 
It will sort the list and return itself in an increasing order.
"""


def MergeSort(listToSort):

    # First, identify whether the length of the list is larger than 1.
    # If not, just return it.
    if len(listToSort) > 1:

        # divide the list into two parts
        divide = len(listToSort) // 2
        left_part = listToSort[:divide]
        right_part = listToSort[divide:]
        MergeSort(left_part)
        MergeSort(right_part)

        # Declear three indexes
        i = 0  # the index of the left_part
        j = 0  # the index of the right_part
        k = 0  # the index of the original list

        # Merge the two parts
        # If i is smaller than the length of left_part
        # and j is smaller than the length of right_part, the loop continues
        # Iterate through two parts.
        # Compare the smallest elements of two parts,
        # add them to the original list.
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                listToSort[k] = left_part[i]
                i += 1
                pass
            else:
                listToSort[k] = right_part[j]
                j += 1
                pass
            k += 1
            pass

        # If some elements left in left_part, add them to the original list.
        for key in range(i, len(left_part)):
            listToSort[k] = left_part[key]
            k += 1

        # If some elements left in right_part, add them to the original list.
        for key in range(j, len(right_part)):
            listToSort[k] = right_part[key]
            k += 1

        return listToSort


"""
5. QuickSort
The function is an implementation of bubble sorting algorithm.
The function could sort an input list of numbers and return it.
Its input is a list of numbers. 
It will sort the list and return itself in an increasing order.
"""


def QuickSort(listToSort, i=0, j=None):

    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
        pass

    # If j equals the length of the original list, set j equals to j-1.
    # This is for the convenience of the following code.
    if j == len(listToSort):
        j = j-1
        pass
    else:
        pass

    # If i is larger or equal to j, return nothing.
    if i >= j:
        return None

    # set the pivot, the left index and the right index
    pivot = listToSort[j]
    left = i
    right = j-1

    # If left index is smaller or equal to right index, the loop continues.
    # Put everything smaller than the pivot in front
    # and everything larger than the pivot in back.
    # Resurse on each partition.
    while left <= right:

        while listToSort[left] < pivot:
            left += 1
            pass

        while listToSort[right] > pivot:
            right -= 1
            pass

        if left <= right:
            listToSort[left], listToSort[right] \
                = listToSort[right], listToSort[left]
            left += 1
            right -= 1

    listToSort[left], listToSort[j] \
        = listToSort[j], listToSort[left]

    # Do the same thing above by call the QuickSort function and set new i and j.
    QuickSort(listToSort, i, left-1)
    QuickSort(listToSort, left + 1, j)

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
    measureTime()
