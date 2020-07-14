"""
Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# approach: small brain recursion, record, compare
# memory: O(p+q)
# runtime: O(2p+2q)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        pTree = []
        qTree = []
        
        self.traverseNode(pTree, p)
        self.traverseNode(qTree, q)
        
        if len(pTree) != len(qTree):
            return False
        
        for i in range(len(pTree)):
            if pTree[i] != qTree[i]:
                return False
       
        return True


    def traverseNode(self, tree: List, node: TreeNode):
        if node:
            tree.append(node.val)
            self.traverseNode(tree, node.left)
            self.traverseNode(tree, node.right)
        else:
            tree.append(None)


# approach: big brain recursion and compare
# memory: O(1)
# runtime: O(p+q)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
                
        if not p and not q:
            return True

        if p and q:
            if p.val != q.val:
                return False
        else:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
