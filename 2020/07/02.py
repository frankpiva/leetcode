"""
Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
"""

# approach: iterate through every node
# memory: O(V)
# runtime: O(V)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.count = 0
        if root == None:
            return []
        else:
            self.bottomUp = []
            self.traverseNode(0, root)
            return self.bottomUp[::-1]
        
    def traverseNode(self, level, node):
        nextLevel = level + 1
        if len(self.bottomUp) < nextLevel:
            self.bottomUp.append([])
        self.bottomUp[level].append(node.val)
        if node.left != None:
            self.traverseNode(nextLevel, node.left)
        if node.right != None: 
            self.traverseNode(nextLevel, node.right)
