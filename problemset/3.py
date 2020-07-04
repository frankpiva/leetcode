"""
3. Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

# approach: brute force with a short circuit
# memory: O(n)
# runtime: O(n*(n+1)/2 - 1) <-- gross, but I'm lazy
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum = 0
        for i in range(0, len(s)):
            dictionary = {}
            for j in range(i, len(s)):
                character = s[j]
                if character not in dictionary:
                    dictionary[character] = True
                else:
                    break
                maximum = max(maximum, len(dictionary))
            if maximum >= len(s) - i:
                return maximum
        return maximum