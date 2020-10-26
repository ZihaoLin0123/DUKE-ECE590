"""
Math 560
Project 1
Fall 2020

Partner 1: Han Gong
Partner 2: Xueyang Liu
Date: 10/4/2020
"""

"""
SelectionSort
"""


def SelectionSort(listToSort):

	for i in range(len(listToSort)):
		mini = listToSort[i]
		minIndex = i
		for j in range(len(listToSort[i:])):
			if(listToSort[i+j]<mini):
				minIndex = i+j
				mini = listToSort[i+j]
		swap(listToSort,minIndex,i)
	return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
	if(len(listToSort)==1 or len(listToSort)==0):
		return listToSort
	for i in range(1,len(listToSort)):
		temp = listToSort[i]
		rest = i-1
		while rest>=0 and temp<listToSort[rest]:
			listToSort[rest+1] = listToSort[rest]
			rest-=1
		listToSort[rest+1] = temp
	return listToSort



"""
BubbleSort
"""
def BubbleSort(listToSort):
    swapped = True
    while swapped:
    	swapped = False
    	for i in range(len(listToSort)-1):
    		if(listToSort[i]>listToSort[i+1]):
    			swap(listToSort,i,i+1)
    			swapped = True
    return listToSort

"""
MergeSort
"""
def MergeSort(listToSort):
	if(len(listToSort)==0 or len(listToSort)==1):
		return listToSort
	elif(len(listToSort)==2):
		if(listToSort[0]>listToSort[1]):
			swap(listToSort,0,1)
		return listToSort
	else:
		# divide the list into 2 parts 
		mid = len(listToSort)//2
		# sort the 2 parts respectively, recursively
		left = MergeSort(listToSort[:mid])
		right = MergeSort(listToSort[mid:])
		# merge the two sorted part into a whole sorted list
		leftIndex,rightIndex = 0,0
		insertIndex = 0
		while insertIndex<=len(listToSort)-1:
			if(leftIndex==mid):
				listToSort[insertIndex] = right[rightIndex]
				rightIndex+=1
			elif(rightIndex==len(listToSort)-mid):
				listToSort[insertIndex] = left[leftIndex]
				leftIndex+=1
			elif(left[leftIndex]<=right[rightIndex]):
				listToSort[insertIndex] = left[leftIndex]
				leftIndex+=1
			else:
				listToSort[insertIndex] = right[rightIndex]
				rightIndex+=1
			insertIndex+=1
	return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
	# Set default value for j if None.
	if j == None:
		j = len(listToSort)
	if j-i == 0 or j-i ==1:
		return listToSort
	if i<j:
		#initialize index and value for pivot
		pValue,p = 0,0
		# use median of i.j-1,mid for pivot
		mid = len(listToSort[i:j])//2 + i
		a,b,c = listToSort[i],listToSort[mid],listToSort[j-1]
		if((a<=b and b<=c) or (c<=b and b<=a)):
			p,pValue = mid,listToSort[mid]
		elif((b<=a and a<=c) or(c<=a and a<=b)):
			p,pValue = i,listToSort[i]
		else:
			p,pValue = j-1,listToSort[j-1]
		
		# swap pivot to the end of list and then partition the list based on the pivot
		swap(listToSort,j-1,p)
		writeHead = i
		for k in range(i,j-1):
			if(listToSort[k]<=pValue):
				swap(listToSort,writeHead,k)
				writeHead+=1
		swap(listToSort,writeHead,j-1)
		# now the list is partitioned by the pivot
		# call quicksort to the left part and the right part respectively
		p = writeHead
		QuickSort(listToSort,i,p)
		QuickSort(listToSort,p+1,j)
	return listToSort
"""
Swap

Swap the ith and jth element in lst in place
"""
def swap(lst,i,j):
	lst[i],lst[j] = lst[j],lst[i]
	return lst



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
