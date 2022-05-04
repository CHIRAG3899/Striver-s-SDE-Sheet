#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
#You must solve this problem without using the library's sort function.
#
#Example 1:
#Input: nums = [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]

#Example 2:
#Input: nums = [2,0,1]
#Output: [0,1,2]

class Solution:
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # constant for colors
        RED, WHITE, BLUE = 0, 1, 2
        
        # two pointers for RED as well as BLUE
        idx_red, idx_blue = 0, len(nums)-1
        
        i = 0
        while i <= idx_blue :
            
            if nums[i] == RED:
                
                nums[idx_red], nums[i] = nums[i], nums[idx_red]
                
                # update idx for red
                idx_red += 1
            
            
            elif nums[i] == BLUE:
            
                nums[idx_blue], nums[i] = nums[i], nums[idx_blue]
                
                # update idx for blue
                idx_blue -= 1
                
                # i-1 in order to stay and do one more color check on next iteration
                i -= 1
            
            
            # i move forward
            i += 1

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    # 11:37
    def sortColors(self, A):
        i, j, n = 0, 0, len(A) - 1
        
        while j <= n:
            if A[j] < 1:
                A[i], A[j] = A[j], A[i]
                i += 1
                j += 1
            elif A[j] > 1:
                A[j], A[n] = A[n], A[j]
                n -= 1
            else:
                j += 1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        d={}
        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        x=0
        for i in sorted(d):
            for j in range(d[i]):
                nums[x+j]=i
            x=x+d[i]