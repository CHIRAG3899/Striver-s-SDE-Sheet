#Given an array containing both positive and negative integers, we have to find the length of the longest subarray with the sum of all elements equal to zero.
#
#Example 1:
#
#Input Format: N = 6, array[] = {9, -3, 3, -1, 6, -5}
#
#Result: 5
#
#Explanation: The following subarrays sum to zero:
#{-3, 3} , {-1, 6, -5}, {-3, 3, -1, 6, -5}
#Since we require the length of the longest subarray, our answer is 5!
#Example 2:
#
#Input Format: N = 8, array[] = {6, -2, 2, -8, 1, 7, 4, -10}
#
#Result: 8
#
#Subarrays with sum 0 : {-2, 2}, {-8, 1, 7}, {-2, 2, -8, 1, 7}, {6, -2, 2, -8, 1, 7, 4, -10}
#Length of longest subarray = 8
#Example 3:
#
#Input Format: N = 3, array[] = {1, 0, -5}
#
#Result: 1
#
#Subarray : {0}
#Length of longest subarray = 1
#Example 4:
#
#Input Format: N = 5, array[] = {1, 3, -5, 6, -2}
#
#Result: 0
#
#Subarray: There is no subarray that sums to zero

def maxLen(arr): 
      
    # initialize result 
    max_len = 0
  
    # pick a starting point 
    for i in range(len(arr)): 
          
        # initialize sum for every starting point 
        curr_sum = 0
          
        # try all subarrays starting with 'i' 
        for j in range(i, len(arr)): 
          
            curr_sum += arr[j] 
  
            # if curr_sum becomes 0, then update max_len 
            if curr_sum == 0: 
                max_len = max(max_len, j-i+1) 
  
    return max_len 


# Returns the maximum length 
def maxLen(arr): 
      
    # NOTE: Dictonary in python in implemented as Hash Maps 
    # Create an empty hash map (dictionary) 
    hash_map = {} 
  
    # Initialize result 
    max_len = 0
  
    # Initialize sum of elements 
    curr_sum = 0
  
    # Traverse through the given array 
    for i in range(len(arr)): 
          
        # Add the current element to the sum 
        curr_sum += arr[i] 
  
        if arr[i] is 0 and max_len is 0: 
            max_len = 1
  
        if curr_sum is 0: 
            max_len = i+1
  
        # NOTE: 'in' operation in dictionary to search  
        # key takes O(1). Look if current sum is seen  
        # before 
        if curr_sum in hash_map: 
            max_len = max(max_len, i - hash_map[curr_sum] ) 
        else: 
  
            # else put this sum in dictionary 
            hash_map[curr_sum] = i 
  
    return max_len