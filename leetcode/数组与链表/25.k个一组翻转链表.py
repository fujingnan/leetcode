# Definition for singly-linked list.
"""
https://leetcode.cn/problems/reverse-nodes-in-k-group/
解题思路：https://leetcode.cn/problems/reverse-nodes-in-k-group/solution/tong-su-li-jie-by-xiao-fu-de-fu-b6rm/

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next or k == 1:
            return head
        stack = []
        resLink = ListNode(None)
        p = resLink
        while head:
            # 易错：容易把if条件前置
            stack.append(head.val)
            head = head.next
            if len(stack) == k:
                while stack:
                    p.next = ListNode(stack.pop())
                    p = p.next
        if stack:
            for v in stack:
                p.next = ListNode(v)
                # 易忘
                p = p.next
        return resLink.next