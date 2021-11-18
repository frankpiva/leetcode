"""
62. Unique Paths
Medium

7114

267

Add to List

Share
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.
"""

# approach: dynamic programming
# memory: O(m * n)
# runtime: O(m * n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lookup = [[1 for i in range(n)] for j in range(m)]
        for row in range(m):
            for col in range(n):
                if row > 0 and col > 0: # add the top and left
                    lookup[row][col] = lookup[row - 1][col] + lookup[row][col - 1]
        return lookup[-1][-1]
