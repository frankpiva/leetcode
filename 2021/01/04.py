"""
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = []
Output: []

Example 3:

Input: l1 = [], l2 = [0]
Output: [0]

 

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both l1 and l2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# approach: anchor head, compare, merge, attach leftovers
# memory: O(1)
# runtime: O(n)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # short circuit: empty list cases
        if not l1 and not l2:
            return l1
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        # set the head, advance next pointer
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
            
        # set this
        this = head
        
        # merge lists
        while l1 and l2:
            if l1.val < l2.val:
                this.next = l1
                this = l1
                l1 = l1.next
            else:
                this.next = l2
                this = l2
                l2 = l2.next
                
        # attach dangling lists if they are left over
        if l1 and not l2:
            this.next = l1
            
        if l2 and not l1:
            this.next = l2
        
        return head