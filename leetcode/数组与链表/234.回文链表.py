"""
解题思路：https://leetcode.cn/problems/palindrome-linked-list/solution/tong-su-li-jie-hui-wen-lian-biao-wen-ti-lej9q/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not (head or head.next):
            return True
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        fast = slow.next
        slow.next = None
        while fast:
            prev = fast.next
            fast.next = slow
            slow = fast
            fast = prev
        fast = slow
        slow = head
        while slow:
            if not fast.val == slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True