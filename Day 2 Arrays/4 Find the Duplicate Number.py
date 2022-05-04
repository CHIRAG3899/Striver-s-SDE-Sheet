#Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
#There is only one repeated number in nums, return this repeated number.
#
#You must solve the problem without modifying the array nums and uses only constant extra space.
#
# 
#
#Example 1:
#
#Input: nums = [1,3,4,2,2]
#Output: 2
#Example 2:
#
#Input: nums = [3,1,3,4,2]
#Output: 3

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
            
class Solution:
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break
           
        slow = nums[0];
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow