#Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

#Example 1:
#Input: nums = [3,2,3]
#Output: [3]

#Example 2:
#Input: nums = [1]
#Output: [1]

#Example 3:
#Input: nums = [1,2]
#Output: [1,2]

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3
        count = {}
        out=[]
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for i in count:
            if count[i]>n:
                out.append(i)
        return out

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        non_duplicate = list(set(nums))
        output = []
        for i in non_duplicate:
            if nums.count(i) > (len(nums)/3):
                output.append(i)
        return output