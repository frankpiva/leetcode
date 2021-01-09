"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""

# approach: iterate with a stack
# memory: O(n)
# runtime: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        complements = { ')': '(', ']': '[', '}': '{' }
        stack = []
        
        # iterate through every character
        for c in s:
            if c == '(' or c == '{' or c =='[':
                stack.append(c)
            else:
                # check if there is a value to pop
                if len(stack) > 0:
                    # check if the value lines up
                    if stack[-1] == complements[c]:
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False
        
        # check for leftover values
        if len(stack) > 0:
            return False
        
        return True
                