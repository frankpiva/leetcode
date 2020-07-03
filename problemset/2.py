"""
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# approach: iterative processing
# memory: (n)
# runtime: (2n)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.processList(l1)
        n2 = self.processList(l2)
        answer = str(n1 + n2)[::-1]
        l3 = ListNode(answer[0], None)
        temp = l3
        for e in answer[1:]:
            temp.next = ListNode(e, None)
            temp = temp.next
        return l3
        
    def processList(self, ln):
        numbers = []
        while ln != None:
            numbers.append(ln.val)
            ln = ln.next
        numbers = numbers[::-1]
        word = ''
        for number in numbers:
            word += str(number)
        return int(word)