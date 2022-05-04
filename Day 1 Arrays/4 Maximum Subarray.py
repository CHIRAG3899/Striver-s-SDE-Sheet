#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
#A subarray is a contiguous part of an array.
#
#Example 1:
#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.
#
#Example 2:
#Input: nums = [1]
#Output: 1
#
#Example 3:
#Input: nums = [5,4,-1,7,8]
#Output: 23

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #meh = max ending here & msf = max so far
        meh = 0
        msf = nums[0]
        for i in nums:  
            #Add every element to meh
            meh += i
		#Replace if greater than msf
            if(meh > msf):
                msf = meh
			
		#If negative make meh = 0
            if(meh < 0):
                meh = 0
        return msf

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = right = 0
        global_max = float('-inf')
        local_sum = 0
        n = len(nums)
        
        while right < n:
            local_sum += nums[right]
            
            if local_sum < nums[right]:
                local_sum = nums[right]
                left = right
            
            global_max = max(global_max, local_sum)
            right += 1
            
            
        return global_max

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = res = nums[0]
        for i in range(1,len(nums)):
            sum = max(nums[i], sum+nums[i])
            res = max(res, sum)
        return res