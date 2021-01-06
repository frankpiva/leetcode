"""
Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]

 

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# approach: recursion with pointer for look ahead
# memory: O(n)
# runtime: O(n)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # need two nodes for duplicates to exist
        if not head or not head.next:
            return head
        # check for duplicates
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head
        # remove duplicates
        this = head
        while this and this.val == head.val:
            this = this.next
        return self.deleteDuplicates(this)
                    
        