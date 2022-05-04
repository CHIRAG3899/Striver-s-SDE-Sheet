#Given an integer numRows, return the first numRows of Pascal's triangle.
#
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#Example 1:
#Input: numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
#Example 2:
#Input: numRows = 1
#Output: [[1]]

class Solution:
    def generate(self, numRows):
        result, row = [[1]], 1
        while row<numRows:
            result.append([1])
            for i in range(1,row):
                result[row].append(result[row-1][i-1] + result[row-1][i])
            result[row].append(1)
            row += 1
        return result