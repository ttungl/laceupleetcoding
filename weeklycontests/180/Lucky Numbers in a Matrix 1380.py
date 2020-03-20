# 1380. Lucky Numbers in a Matrix

# Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.


# Example 1:

# Input: matrix = [[3,7,8],
# 				 [9,11,13],
# 				 [15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
# Example 2:

# Input: matrix = [[1,10,4,2],
# 				 [9,3,8,7],
# 				 [15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 3:

# Input: matrix = [[7,8],[1,2]]
# Output: [7]



class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # sol1: brute-force
        # time O(n*m) space O(n+m)
        # runtime: 204ms; mem: 13.1mb
        res = []
        rows, cols = len(matrix), len(matrix[0])
        maxcols = [max(i) for i in zip(*matrix)] # transpose matrix
        for i in range(rows):
            for j in range(cols):
                x = matrix[i][j]
                minrow = min(matrix[i][:])
                maxcol = maxcols[j]  # max value at the j-th column in matrix
                if (x == minrow) and (x >= maxcol): 
                    res.append(x)
        return res
        
        
        # sol 2: 
        # time O(m*n) space O(n+m)
        # runtime: 132ms; mem: 13.2mb
        minrows = [min(i) for i in matrix]
        maxcols = [max(i) for i in zip(*matrix)] # transpose matrix
        return [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0])) if minrows[i]==maxcols[j]]
        
        


