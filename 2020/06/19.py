"""
Longest Duplicate Substring

Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)
Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

Example 1:
Input: "banana"
Output: "ana"

Example 2:
Input: "abcd"
Output: ""

Note:
2 <= S.length <= 10^5
S consists of lowercase English letters.
"""

# naive solution, fails on test #3
class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        max_length = len(S) - 1
        for i in range(max_length, 0, -1):
            possibilities = {}
            max_index = len(S) - i
            for j in range(0, max_index + 1, 1):
                possibility = S[j:i+j]
                print('possibility', possibility)
                try:
                    if possibilities[possibility]:
                        return possibility
                except:
                    possibilities[possibility] = True
        return ""

# binary, fails on test # 12
class Solution(object):    
    def check_next(self, size):
        for i in range(size + 1, self.max_length, 1):
                new_substring = self.substring_exists(i)
                if new_substring == "":
                    break
                else:
                    self.max_substring = new_substring
    
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        print(sys.version)
        self.S = S
        size = 100
        print('size', size)
        self.max_length = len(S) - 1
        self.max_substring = self.substring_exists(size)
        if self.max_substring != "":
            while size < self.max_length / 2:
                size = size * 2
                new_substring = self.substring_exists(size)
                print('substring', substring)
                if new_substring == "":
                    break
            self.check_next(size)
        else:
            while size > 1:
                size = size / 2
                new_substring = self.substring_exists(size)
                if new_substring != "":
                    self.max_substring = new_substring
                    break
            if size != 1:
                self.check_next(size)
        return self.max_substring
            
    def substring_exists(self, size):
        print('substring_exists('+str(size)+')')
        possibilities = {}
        max_index = len(self.S) - size
        for j in range(0, max_index + 1, 1):
            possibility = self.S[j:size+j]
            #print('possibility', possibility)
            try:
                if possibilities[possibility]:
                    return possibility
            except:
                possibilities[possibility] = True
        return ""