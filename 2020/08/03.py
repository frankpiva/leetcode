"""
Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false

 

Constraints:

    s consists only of printable ASCII characters.
"""

# approach: format string, squeeze from both ends with early exit
# memory: O(n) where n is the length of the string
# runtime: O(2n) n to format, n to search
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # quick check:
        if s == '':
            return True

        # everything else
        formatted = re.sub(r'[^a-z0-9]','', s.lower()) # see inverse below
        # formatted = re.sub(r'[\ \_\-\,\:\.\;\?\!\@\#\(\)\{\}\[\]\`\'\"]','', s.lower())
        leftIndex = 0
        rightIndex = len(formatted) - 1
        while leftIndex <= rightIndex:
            if not formatted[leftIndex] == formatted[rightIndex]:
                return False
            leftIndex += 1
            rightIndex -= 1

        return True
