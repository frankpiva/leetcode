"""
Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

# approach: dynamic programming
# memory: O(n)
# runtime: O(n^3/2)
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        
        # short circuit case: 0 <= n <= 3
        if 0 <= n <= 3: return n
        
        # short circuit case: perfect square
        sqrt = int(math.sqrt(n))
        if sqrt*sqrt == n: return 1
            
        # create a lookup table for dynamic programming
        lt = list(range(0,n+1))
            
        # populate lookup table
        for i in range(4, n+1):
            j = 1
            while j*j < n:
                lt[i] = min(lt[i], lt[i-j*j]+1)
                j += 1
                
        # return value for n
        return lt[n]