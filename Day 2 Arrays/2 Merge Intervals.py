#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
# 
#
#Example 1:
#
#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#Example 2:
#
#Input: intervals = [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

from heapq import heappop, heappush
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        heap =[]
        res = []
        intervals.sort()
        for i in intervals:
            if not heap:
                heapq.heappush(heap, i)
            elif heap[0][1]>=i[0]:
                    m, n = heapq.heappop(heap)
                    
                    heapq.heappush( heap, [min(m, i[0]), max(i[1], n)])
            else:
                res.append(heapq.heappop(heap))
                heapq.heappush(heap, i)
        
        if heap:
            res.extend(heap)
        print(res)
        return res