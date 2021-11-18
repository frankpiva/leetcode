"""
668. Kth Smallest Number in Multiplication Table
Hard

1418

41

Add to List

Share
Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

 

Example 1:


Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.
Example 2:


Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.
 

Constraints:

1 <= m, n <= 3 * 104
1 <= k <= m * n
"""

# approach:
# memory:
# runtime:
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        high = m * n
        low = 1
        while low <= high:
            mid = (high - low) // 2 + low
            if self.count(m, n, mid) >= k:
                high = mid - 1
            else:
                low = mid + 1
        return low
    
    def count(self, m: int, n: int, mid: int):
        count = 0
        for i in range(1, m + 1):
            count += min(n, mid // i)
        return count            
