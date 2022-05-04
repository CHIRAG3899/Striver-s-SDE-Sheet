#Given an integer array nums, return the number of reverse pairs in the array.
#
#A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].
#
# 
#
#Example 1:
#
#Input: nums = [1,3,2,3,1]
#Output: 2
#Example 2:
#
#Input: nums = [2,4,3,5,1]
#Output: 3

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        cnt = 0

        def merge(left, right):
            nonlocal cnt
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= 2*right[j]:
                    i += 1
                else:
                    cnt += len(left)-i
                    j += 1

            return sorted(left+right)


        def mergeSort(A):
            if len(A) <= 1:
                return A
            return merge(mergeSort(A[:(len(A) + 1) // 2]), mergeSort(A[(len(A) + 1) // 2:]))

        mergeSort(nums)
        return cnt

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def recursiveFunction(lowerIndex = 0, upperIndex = len(nums) - 1):
            
            if lowerIndex >= upperIndex:
                return 0
            
            midIndex = (lowerIndex + upperIndex) // 2
            count = recursiveFunction(lowerIndex, midIndex) + recursiveFunction(midIndex + 1, upperIndex)
            
            index_i = lowerIndex
            for rightNumber in nums[midIndex + 1: upperIndex + 1]:
                while index_i <= midIndex and nums[index_i] <= rightNumber * 2:
                    index_i += 1
                count += midIndex + 1 - index_i
                if index_i > midIndex:
                    break
            
            nums[lowerIndex: upperIndex + 1] = sorted(nums[lowerIndex: upperIndex + 1])
			
            return count
        
        return recursiveFunction()

def reversePairs(self, nums: List[int]) -> int:
        res = 0
        sorted_values = []
        for j in range(len(nums)):
            i = bisect.bisect_right(sorted_values, 2 * nums[j])
            res += (j - i)
            bisect.insort(sorted_values, nums[j])
        return res