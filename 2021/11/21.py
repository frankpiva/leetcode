"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

3726

63

Add to List

Share
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.inorder = inorder
        self.postorder = postorder
        return self.buildNextNode(0, len(inorder) - 1)


    def buildNextNode(self, start: int, end: int) -> Optional[TreeNode]:
        if start > end:
            return None
        else:
            root = TreeNode(self.postorder.pop())
            index = self.inorder.index(root.val)
            root.right = self.buildNextNode(index + 1, end)
            root.left = self.buildNextNode(start, index - 1)
            return root
