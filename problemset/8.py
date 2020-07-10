"""
8. String to Integer (atoi)
Medium

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:

Input: "42"
Output: 42

Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""

# approach: small brain lazy convert, passed 228/1079 test cases
# memory: O(1)
# runtime: O(1)
class Solution:
    def myAtoi(self, str: str) -> int:
        bigpint = 2**31 - 1
        bignint = -(2**31)
        words = str.split(' ')
        for word in words:
            if word == '':
                continue
            try:
                num = int(float(word))
                if  num > bigpint:
                    return bigpint
                elif num < bignint:
                    return bignint
                else:
                    return num
            except:
                return 0
        return 0


# approach: slow brain iterate and detect bad input
# memory: O(n)
# runtime: O(n)
class Solution:
    def myAtoi(self, str: str) -> int:
        bigpint = 2**31 - 1
        bignint = -(2**31)
        allowedToSet = True
        digits = ''
        sign = 1

        for c in str:
            # already captured first number group
            if (len(digits) > 0) and (c not in '0123456789'):
                break

            # sign, but no numbers
            if not allowedToSet and c == ' ':
                return 0

            # skip spaces
            if c == ' ':
                continue

            # set the sign flag
            if c == '-' or c == '+':
                if allowedToSet == True:
                    allowedToSet = False
                    sign = -1 if c == '-' else 1
                    continue
                else:
                    return 0

            # check for letters, punctuation, etc.
            try:
                if int(c) in range(0,10):
                    digits += c
            except:
                break

        if len(digits) > 0:
            num = int(digits) * sign
            if num > bigpint:
                return bigpint
            elif num < bignint:
                return bignint
            else:
                return num

        return 0
