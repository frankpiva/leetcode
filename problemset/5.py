"""
5. Longest Palindromic Substring
Medium

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""

# naive attempt, largest to smallest, passed 41/103 test cases
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # short circuit case: ""
        if s == "": return ""
        
        palindrome = []
        for i in range(0, len(s)):
            for j in range(0, i+1):
                palindrome = s[j:len(s)-i+j]
                
                # check palindrome
                isPalindrome = True
                for k in range(0, len(palindrome)):
                    if palindrome[k] != palindrome[-(k+1)]:
                        isPalindrome = False
                if isPalindrome: return palindrome

# naive attempt, smallest to largest, passed 88/103 test cases
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # short circuit case: ""
        if s == "": return ""
        
        maximum = ''
        for i in range(0, len(s)):
            for j in range(0, len(s) - i):
                candidate = s[j:i+j+1]
                
                # check palindrome
                isPalindrome = True
                for k in range(0, len(candidate)):
                    if candidate[k] != candidate[-(k+1)]:
                        isPalindrome = False
                if isPalindrome:
                    if len(candidate) > len(maximum):
                        maximum = candidate
                        break # go to next length

            # short circuit case: no new max was found
            if i-1 > len(maximum):
                return maximum
                        
        return maximum

# approach: middle out expansion
# memory: O(1)
# runtime: O(nlog(n)) ? <-- need to check this
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # short circuit case: ""
        if s == "": return ""
        
        # short circuit case: "x"
        if len(s) == 1: return s
            
        # everything else
        leftIndex, rightIndex = 0, 0
        for i in range(0, len(s)):
            candidate1 = self.expandFromMiddle(s, i, i)
            candidate2 = self.expandFromMiddle(s, i, i+1)
            maximum = max(candidate1, candidate2)
            if maximum > rightIndex - leftIndex:
                leftIndex = i - int((maximum - 1) / 2)
                rightIndex = i + int(maximum / 2)

        return s[leftIndex:rightIndex + 1]

    
    def expandFromMiddle(self, string, leftIndex, rightIndex):
        while leftIndex >= 0 and rightIndex < len(string) and string[leftIndex] == string[rightIndex]:
            leftIndex -= 1
            rightIndex += 1
        return rightIndex - leftIndex - 1
