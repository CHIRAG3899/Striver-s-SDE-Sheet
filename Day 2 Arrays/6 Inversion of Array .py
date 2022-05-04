#Inversion Count for an array indicates – how far (or close) the array is from being sorted. If the array is already sorted, then the inversion count is 0, but if the array is sorted in the reverse order, the inversion count is the maximum. 
#Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j 
#Example: 
#
#Input: arr[] = {8, 4, 2, 1}
#Output: 6
#
#Explanation: Given array has six inversions:
#(8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).
#
#
#Input: arr[] = {3, 1, 2}
#Output: 2
#
#Explanation: Given array has two inversions:
#(3, 1), (3, 2) 

def getInvCount(arr, n):
 
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1
 
    return inv_count

from heapq import heappush, heappop
from bisect import bisect, insort
 
 
def getNumOfInversions(A):
    N = len(A)
    if N <= 1:
        return 0
 
    sortList = []
    result = 0
 
    # heapsort, O(N*log(N))
    for i, v in enumerate(A):
        heappush(sortList, (v, i))
 
    x = []  # create a sorted list of indexes
    while sortList:  # O(N)
        v, i = heappop(sortList)  # O(log(N))
        # find the current minimum's index
        # the index y can represent how many minimums on the left
        y = bisect(x, i)  # O(log(N))
        # i can represent how many elements on the left
        # i - y can find how many bigger nums on the left
        result += i - y
 
        insort(x, i)  # O(log(N))
 
    return result

