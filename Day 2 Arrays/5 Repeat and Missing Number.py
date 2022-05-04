#You are given a read only array of n integers from 1 to n.
#
#Each integer appears exactly once except A which appears twice and B which is missing.
#
#Return A and B.
#
#Example:
#
#Input:[3 1 2 5 3] 
#
#Output:[3, 4] 
#
#A = 3, B = 4

def printTwoElements( arr, size):
    for i in range(size):
        if arr[abs(arr[i])-1] > 0:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
        else:
            print("The repeating element is", abs(arr[i]))
              
    for i in range(size):
        if arr[i]>0:
            print("and the missing element is", i + 1)

def repeatedNumber(A):
      
    length = len(A)
    Sum_N = (length * (length + 1)) // 2
    Sum_NSq = ((length * (length + 1) * 
                     (2 * length + 1)) // 6)
      
    missingNumber, repeating = 0, 0
      
    for i in range(len(A)):
        Sum_N -= A[i]
        Sum_NSq -= A[i] * A[i]
          
    missingNumber = (Sum_N + Sum_NSq // 
                             Sum_N) // 2
    repeating = missingNumber - Sum_N
      
    ans = []
    ans.append(repeating)
    ans.append(missingNumber)
      
    return ans

