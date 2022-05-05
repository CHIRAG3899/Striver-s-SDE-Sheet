#Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to B.
#
#Examples:
#
#Input Format:  A = [4, 2, 2, 6, 4] , B = 6
#Result: 4
#Explanation: The subarrays having XOR of their elements as 6 are  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]
#
#Input Format: A = [5, 6, 7, 8, 9], B = 5
#Result: 2
#Explanation:The subarrays having XOR of their elements as 2 are [5] and [5, 6, 7, 8, 9]

def subarrayXor(arr, n, m):
    ans = 0 # Initialize ans
  
    # Pick starting point i of subarrays
    for i in range(0,n):
         
        xorSum = 0 # Store XOR of current subarray
  
        # Pick ending point j of subarray for each i
        for j  in range(i,n):
            # calculate xorSum
            xorSum = xorSum ^ arr[j]
  
            # If xorSum is equal to given value,
            # increase ans by 1.
            if (xorSum == m):
                ans+=1
    return ans

def subarrayXor(arr, n, m):
 
    ans = 0 # Initialize answer to be returned
 
    # Create a prefix xor-sum array such that
    # xorArr[i] has value equal to XOR
    # of all elements in arr[0 ..... i]
    xorArr =[0 for _ in range(n)]
 
    # Create map that stores number of prefix array
    # elements corresponding to a XOR value
    mp = dict()
 
    # Initialize first element
    # of prefix array
    xorArr[0] = arr[0]
 
    # Computing the prefix array.
    for i in range(1, n):
        xorArr[i] = xorArr[i - 1] ^ arr[i]
 
    # Calculate the answer
    for i in range(n):
         
        # Find XOR of current prefix with m.
        tmp = m ^ xorArr[i]
 
        # If above XOR exists in map, then there
        # is another previous prefix with same
        # XOR, i.e., there is a subarray ending
        # at i with XOR equal to m.
        if tmp in mp.keys():
            ans = ans + (mp[tmp])
 
        # If this subarray has XOR
        # equal to m itself.
        if (xorArr[i] == m):
            ans += 1
 
        # Add the XOR of this subarray to the map
        mp[xorArr[i]] = mp.get(xorArr[i], 0) + 1
 
    # Return total count of subarrays having
    # XOR of elements as given value m
    return ans

from collections import defaultdict
def subarrayXor(arr, n, m):
    HashTable=defaultdict(bool)
    HashTable[0]=1
    count=0
    curSum=0
    for i in arr:
        curSum^=i
        if HashTable[curSum^m]:
            count+=HashTable[curSum^m]
        HashTable[curSum]+=1
    return(count)