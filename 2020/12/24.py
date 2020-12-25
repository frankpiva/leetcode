"""
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.

 

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]

 

Constraints:

    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# approach: look ahead and swap
# runtime: O(n)
# memory: O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # point to head
        this = head
        
        # check that this node and next node exist
        while this and this.next:
            t = this.val
            this.val = this.next.val
            this.next.val = t
            
            # look ahead two nodes: update pointer or exit
            if this.next.next:
                this = this.next.next
            else:
                break
        
        return head
