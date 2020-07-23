"""
Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# approach: iterate, store, iterate, update, return
# memory: O(n)
# runtime: O(n + n / 2)
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root:
            self.levels = []
            self.traverseNode(0, root)
            for i in range(len(self.levels)):
                if i % 2 == 1:
                    self.levels[i] = reversed(self.levels[i])
            return self.levels
        else:
            return root

    def traverseNode(self, level: int, node: TreeNode):
        if len(self.levels) == level:
            self.levels.append([])
        self.levels[level].append(node.val)
        if node.left:
            self.traverseNode(level + 1, node.left)
        if node.right:
            self.traverseNode(level + 1, node.right)
