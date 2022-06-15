# Definition for singly-linked list.
"""
https://leetcode.cn/problems/sort-list/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        # 易忘
        slow.next = None
        h1 = self.sortList(head)
        h2 = self.sortList(mid)
        node = ListNode(None)
        p = node
        while h1 and h2:
            if h1.val < h2.val:
                p.next = ListNode(h1.val)
                h1 = h1.next
            else:
                p.next = ListNode(h2.val)
                h2 = h2.next
            p = p.next
        if h1:
            p.next = h1
        if h2:
            p.next = h2
        return node.next