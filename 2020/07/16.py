"""
Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

Example 2:

Input: 2.10000, 3
Output: 9.26100

Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:

    -100.0 < x < 100.0
    n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""

# approach: check special cases, iterate until negligible
# memory: O(1)
# runtime: O(n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # short circuit case: x = -1
        if x == -1.0:
            if n % 2 == 0:
                return 1.0
            else:
                return -1.0
        
        # short circuit case: x = 1
        if x == 1.0:
            return x
        
        # short circuit case: n = 0
        if n == 0:
            return 1
        
        # all other cases
        temp = 1.0
        if n > 0:
            for i in range(n):
                if temp == 0:
                    return temp
                temp *= x
            return temp
        else:
            for i in range(n * -1):
                if (1 / temp) < 0.00001:
                    return 0
                temp *= x
            return 1 / temp
