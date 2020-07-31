"""
Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

# approach: dynamic programming with memoization
# memory: O(l * n) where l is the length of the word, and n is the number of solutions
# runtime: O(n) where n is the number of words in the dicitonary
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s, wordDict, {})

    def helper(self, string: str, dictionary: List[str], memo: {}) -> List[str]:
        # memoization optimization
        if string in memo:
            return memo[string]

        # initialize results list
        results = []

        # base case
        if len(string) == 0:
            results.append('')
            return results

        # start checking for words
        for word in dictionary:
            # string begins with the word
            if word == string[:len(word)]:
                # splice out the substring portion after the word
                substring = string[len(word):]
                # recurse with the new substring
                substrings = self.helper(substring, dictionary, memo)
                # build up the list of all possible outcomes
                for substring in substrings:
                    # optional space formatting check
                    if len(substring) == 0:
                        optionalSpace = '' 
                    else:
                        optionalSpace = ' '
                    results.append(word + optionalSpace + substring)

        # memoize the results before return them
        memo[string] = results
        return results
