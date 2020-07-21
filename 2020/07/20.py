"""
Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# approach: use two pointers to splice out nodes
# memory: O(1)
# runtime: O(n)
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # special case: empty list
        if not head:
            return head

        # initialize pointers
        last, this = head, head.next

        # while another node exists
        while this:
            if this.val == val:
                last.next = this.next
                this = this.next
            else:
                last = this
                this = this.next

        # check head
        if head.val == val:
            head = head.next

        return head


# approach: use one pointer to splice out nodes
# memory: O(1)
# runtime: O(n)
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # special case: empty list
        if not head:
            return head

        # initialize pointer
        this = head

        # while another node exists
        while this.next:
            if this.next.val == val:
                this.next = this.next.next
            else:
                this = this.next

        # check head
        if head.val == val:
            return head.next
        else:
            return head
