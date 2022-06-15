# Definition for singly-linked list.
"""
https://leetcode.cn/problems/linked-list-cycle-ii/
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return None
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                meet = slow
                break
        if not fast or not fast.next:
            return None
        slow = head
        while not fast == slow:
            fast = fast.next
            slow = slow.next
        return fast