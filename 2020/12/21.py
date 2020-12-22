"""
Smallest Range II

Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

 

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]

Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]

Example 3:

Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]

 

Note:

    1 <= A.length <= 10000
    0 <= A[i] <= 10000
    0 <= K <= 10000
"""

# approach: divide and conquer
# runtime: n log (n) + n
# memory: c
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        # sort the list, establish reference points
        A.sort()
        global_max = A[-1]
        global_min = A[0]
        optimal_diff = global_max - global_min
        
        # left to right: calculate potential crossovers, update optimal
        for i in range(len(A) - 1):
            potential_max = max(A[i] + K, global_max - K)
            potential_min = min(A[i + 1] - K, global_min + K)
            optimal_diff = min(potential_max - potential_min, optimal_diff)
        
        return optimal_diff
