"""
Reach a Number

You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:

Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

Example 2:

Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.

Note:
target will be a non-zero integer in the range [-10^9, 10^9].
"""

# approach: formula: (n^2 + n) / 2
# runtime: O(n^1/2)
# memory: O(1)
class Solution:
    def reachNumber(self, target: int) -> int:
        # initialize values
        steps = 0
        target = abs(target)
        total = 0
        
        # increment step size and total until total >= target
        while total < target:
            steps += 1
            total += steps
            
        # if difference is even or non-existent: target can be reached in steps
        if (total - target) % 2 == 0:
            return steps
        
        # difference is odd, but steps are even: 1 extra step to adjust
        if steps % 2 == 0:
            return steps + 1
        
        # difference is odd, and steps are odd: 2 extra steps to adjust
        return steps + 2
