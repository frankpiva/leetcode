"""
Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# approach: use postorder to find root, recurse on left and right subtrees
# memory: O(n)
# runtime: O(n)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.helper(len(postorder) - 1, 0, len(inorder) - 1, postorder, inorder)

    def helper(self, postStart, inStart, inEnd, postorder, inorder) -> TreeNode:
        # safety check
        if postStart > len(postorder) - 1 or inStart > inEnd:
            return None

        root = TreeNode(postorder[postStart])

        inIndex = 0
        for index, value in enumerate(inorder):
            if value == root.val:
                inIndex = index

        root.left = self.helper(postStart + inIndex - inEnd - 1, inStart, inIndex - 1, postorder, inorder)
        root.right = self.helper(postStart - 1, inIndex + 1, inEnd, postorder, inorder)

        return root
