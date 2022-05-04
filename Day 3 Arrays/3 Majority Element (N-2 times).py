#Given an array nums of size n, return the majority element.
#
#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#
# 
#
#Example 1:
#
#Input: nums = [3,2,3]
#Output: 3
#Example 2:
#
#Input: nums = [2,2,1,1,1,2,2]
#Output: 2

class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num

class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)import random

class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate