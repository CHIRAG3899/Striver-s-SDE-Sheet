#Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#
# 
#
#Example 1:
#
#Input: x = 2.00000, n = 10
#Output: 1024.00000
#Example 2:
#
#Input: x = 2.10000, n = 3
#Output: 9.26100
#Example 3:
#
#Input: x = 2.00000, n = -2
#Output: 0.25000
#Explanation: 2-2 = 1/22 = 1/4 = 0.25

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        memo = {}      
        def power(x,n):
            if n in memo:return memo[n]
            if n==0: return 1
            elif n==1:return x
            elif n < 0:
                memo[n] = power(1/x,-n)
                return memo[n]
            elif n%2==0:
                memo[n] = power(x*x,n//2)
                return memo[n]
            else:
                memo[n] = x * power(x*x,(n-1)//2)
                return memo[n]
            
        return power(x,n)

class Solution:
    def myPow(self, x, n):
        if abs(x) < 1e-40: return 0 
        if n == 0: return 1
        if n < 0: return self.myPow(1/x, -n)
        lower = self.myPow(x, n//2)
        if n % 2 == 0: return lower*lower
        if n % 2 == 1: return lower*lower*x