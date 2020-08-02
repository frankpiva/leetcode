"""
Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.

 

Example 1:

Input: "USA"
Output: True

 

Example 2:

Input: "FlaG"
Output: False

 

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""

# approach: linear human evaluation
# memory: O(1)
# runtime: O(n)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # check for single letter
        if len(word) <= 1:
            return True

        # check first two letters
        isFirstLetterUppercase = 65 <= ord(word[0]) <= 91
        isSecondLetterUppercase = 65 <= ord(word[1]) <= 91

        # check all the other letters
        isOneOtherLetterUppercase = False
        isOneOtherLetterLowercase = False
        for char in word[2:]:
            if 65 <= ord(char) <= 91:
                isOneOtherLetterUppercase = True
            else:
                isOneOtherLetterLowercase = True

        # check for an incorrect lowercase: XX ... x ...
        if isFirstLetterUppercase and isSecondLetterUppercase:
            if not isOneOtherLetterLowercase:
                return True

        # check for an incorrect uppercase: Xx ... X ...
        if isFirstLetterUppercase and not isSecondLetterUppercase:
            print('made it here')
            if not isOneOtherLetterUppercase:
                return True

        # check for an incorrect uppercase: xx ... X ...
        if not isFirstLetterUppercase and not isSecondLetterUppercase:
            if not isOneOtherLetterUppercase:
                return True

        return False

# approach: linear human evaluation with early exits
# memory: O(1)
# runtime: O(n)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # check for single letter
        if len(word) <= 1:
            return True

        # check first two letters
        isFirstLetterUppercase = 65 <= ord(word[0]) <= 91
        isSecondLetterUppercase = 65 <= ord(word[1]) <= 91
        if not isFirstLetterUppercase and isSecondLetterUppercase:
            return False

        # check all the other letters
        isOneOtherLetterUppercase = False
        isOneOtherLetterLowercase = False
        for char in word[2:]:
            if 65 <= ord(char) <= 91:
                isOneOtherLetterUppercase = True
            else:
                isOneOtherLetterLowercase = True

            # check for an incorrect lowercase: XX ... x ...
            if isFirstLetterUppercase and isSecondLetterUppercase:
                if isOneOtherLetterLowercase:
                    return False

            # check for an incorrect uppercase: Xx ... X ...
            if isFirstLetterUppercase and not isSecondLetterUppercase:
                if isOneOtherLetterUppercase:
                    return False

            # check for an incorrect uppercase: xx ... X ...
            if not isFirstLetterUppercase and not isSecondLetterUppercase:
                if isOneOtherLetterUppercase:
                    return False

        return True
