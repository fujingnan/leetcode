# Definition for singly-linked list.
"""
https://leetcode.cn/problems/linked-list-cycle/
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not (head and head.next):
            return False
        fast = head.next
        slow = head
        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False