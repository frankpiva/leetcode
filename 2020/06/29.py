"""
Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

 

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28

 

Constraints:

    1 <= m, n <= 100
    It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
"""

# approach: dynamic programming
# memory: O(m*n)
# runtime: 0(m*n)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # create and populate a lookup table
        lt = []
        for i in range(0, m):
            lt.append([])
            for j in range(0, n):
                if i == 0 or j == 0:
                    lt[i].append(1)
                else:
                    lt[i].append(lt[i-1][j] + lt[i][j-1])
        return lt[-1][-1]
