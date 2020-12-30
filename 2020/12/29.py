"""
Pseudo-Palindromic Paths in a Binary Tree

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

 

Example 1:

Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:

Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:

Input: root = [9]
Output: 1

 

Constraints:

    The given binary tree will have between 1 and 10^5 nodes.
    Node values are digits from 1 to 9.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# approach: recursion
# memory: O(n)
# runtime: O(n)
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        return self.check_node({}, root)
        
    def check_node(self, lookup: dict, node: TreeNode) -> bool:
        if node:
            # update lookup
            if node.val not in lookup:
                lookup[node.val] = 0
            lookup[node.val] += 1
            
            # check both sides
            left = self.check_node(lookup, node.left)
            right = self.check_node(lookup, node.right)
            
            # clean up lookup
            lookup[node.val] -= 1
            if lookup[node.val] == 0:
                del lookup[node.val]
            
            # check possibilities
            if not node.left and not node.right:
                return max(left, right)
            
            if node.left and node.right:
                return left + right
            
            if node.left:
                return left
            
            if node.right:
                return right
        else:
            # leaf node: evaluate frequencies
            odd_frequency = False
            for value in lookup:
                if lookup[value] % 2 != 0:
                    if odd_frequency:
                        return 0
                    else:
                        odd_frequency = True
            return 1
