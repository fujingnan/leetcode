# Definition for singly-linked list.
from typing import Optional

"""
https://leetcode.cn/problems/merge-two-sorted-lists/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        dummy = ListNode(None)
        p = dummy
        l1, l2 = list1, list2
        while l1 and l2:
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next
            p = p.next
        # 这里容易写错成p.next = ListNode(l1.val)
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return dummy.next