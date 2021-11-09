"""
96. Unique Binary Search Trees
Medium

6144

243

Add to List

Share
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 19
"""

# approach: dynamic programming, lookup table
# memory: O(n)
# runtime: O(n)
class Solution:
    def numTrees(self, n: int) -> int:
        # numTrees(0) = 1
        # numTrees(1) = 1
        lookup = [1] * (n + 1)
        total = 0
            
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += lookup[left] * lookup[right]
            lookup[nodes] = total
        
        return lookup[n]
