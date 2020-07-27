"""
Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

# approach: sum digits, examine modulus
# memory: O(1)
# runtime: O(log(n) + 1)
class Solution:
    def addDigits(self, num: int) -> int:
        # early exit
        if num < 10:
            return num

        word = str(num)
        total = 0
        for char in word:
            total += int(char)

        remainder = total % 9
        if remainder == 0:
            return 9
        else:
            return remainder 

# approach: check for 0, examine modulus
# memory: O(1)
# runtime: O(log(n) + 1)
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        remainder = num % 9
        if remainder == 0:
            return 9
        else:
            return remainder 
