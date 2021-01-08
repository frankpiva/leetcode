"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""

# approach: iterate, build and check substring
# memory: O(n)
# runtime: O(n^2)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        substring = []
        
        # iterate through every letter
        for letter in s:
            # only use portion after index in substring
            if letter in substring:
                index = substring.index(letter)
                substring = substring[index:]
                substring.pop(0)
                substring.append(letter)
            # add letter to subtring, check if maximum
            else:
                substring.append(letter)
                if len(substring) > maximum:
                    maximum = len(substring)
                    
        return maximum
