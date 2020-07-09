"""
7. Reverse Integer
Easy

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

# approach: cast to string, manipulate, cast to int
# memory = O(1)
# runtime = O(1)
class Solution:
    def reverse(self, x: int) -> int:
        bigpint = 2**31 - 1
        bignint = -(2**31)
        word = str(x)
        if word[0] == '-':
            formatted = int((word[-1:0:-1])) * -1
        else:
            formatted = int(word[::-1])
        if bignint <= formatted <= bigpint:
            return formatted
        else:
            return 0
