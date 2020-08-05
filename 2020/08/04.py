"""
Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true

Example 2:

Input: 5
Output: false

Follow up: Could you solve it without loops/recursion?
"""

# approach: examine binary bits
# memory: O(1)
# runtime: O(n^(1/4) + 1)
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # convert to binary, strip off prefix
        bits = bin(num)[2:]

        # powers of 4 have odd numbers of bits
        if len(bits) % 2 == 0:
            return False

        # leftmost bit must be 1
        if not bits[0] == '1':
            return False

        # all other bits must be 0
        for bit in bits[1:]:
            if not bit == '0':
                return False

        # passed all checks, return True
        return True
