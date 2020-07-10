"""
Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# approach: small brain recurse and update
# memory: O(n)
# runtime: O(n)
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # short circuit case: empty tree
        if root == None:
            return 0
        
        self.levels = [[root.val]]
        self.traverseNode(0, root)
        print(self.levels)
        maximum = 0
        for level in self.levels:
            start = -1
            stop = -1
            for ind, val in enumerate(level):
                if val and start == -1:
                    start = ind
                if val:
                    stop = ind
                candidate = stop - start
                print('candidate', candidate, stop, start)
                maximum = max(maximum, stop - start)
        print('maximum', maximum)
        return maximum + 1


    def traverseNode(self, level: int, node: TreeNode) -> int:
        nextLevel = level + 1
        if len(self.levels) <= nextLevel:
            self.levels.append([])
        if node.left:
            self.levels[nextLevel].append(node.left.val)
            self.traverseNode(nextLevel, node.left)
        else:
            self.levels[nextLevel].append(None)
        if node.right:
            self.levels[nextLevel].append(node.right.val)
            self.traverseNode(nextLevel, node.right)
        else:
            self.levels[nextLevel].append(None)


# approach: big brain recurse and update
# memory: O(n), where n = number of levels in the binary tree
# runtime: O(2^n - 1)
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.maxWidth = 0
        self.leftMostPositions = {}
        self.getWidth(root, 0, 0)
        return self.maxWidth


    def getWidth(self, root: TreeNode, depth: int, position: int) -> int:
        # short circuit case: node is null
        if not root:
            return

        # this will only execute when the leftmost node on a level is visited
        if depth not in self.leftMostPositions:
            self.leftMostPositions[depth] = position

        # when this is calculated on rightmost node, it will be a local max
        leftMost = self.leftMostPositions[depth]
        levelWidth = position - leftMost + 1
        self.maxWidth = max(self.maxWidth, levelWidth)
        self.getWidth(root.left, depth + 1, position * 2)
        self.getWidth(root.right, depth + 1, position * 2 + 1)
