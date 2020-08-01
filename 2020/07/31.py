"""
Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

 

Constraints:

    1 <= n <= 45
"""

# approach: dynamic programming
# memory: O(n)
# runtime: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        # initialize lookup list
        lookupList = [0, 1, 2]
        # populate lookup list
        for i in range(3,n+1):
            lookupList.append(lookupList[i-1] + lookupList[i-2])
        # return nth value
        return lookupList[n]

# approach: recursion
# memory: O(1)
# rutnime: O(n)
from functools import lru_cache
class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
