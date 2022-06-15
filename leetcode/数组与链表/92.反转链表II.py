# Definition for singly-linked list.
"""
https://leetcode.cn/problems/reverse-linked-list-ii/
解题思路：https://leetcode.cn/problems/reverse-linked-list-ii/solution/by-xiao-fu-de-fu-up9i/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head.next or left == right:
            return head
        dummy = ListNode(None)
        dummy.next = head
        start = dummy
        for _ in range(left - 1):
            start = start.next
        cur = start.next
        end = cur
        prev = None
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        start.next = prev
        end.next = cur
        return dummy.next
