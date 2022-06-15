# Definition for singly-linked list.
"""
https://leetcode.cn/problems/swap-nodes-in-pairs/
解题思路：https://leetcode.cn/problems/swap-nodes-in-pairs/solution/zhu-guan-by-xiao-fu-de-fu-2ks0/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        dummy = ListNode(None)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            temp = cur.next.next.next
            cur.next.next.next = cur.next
            cur.next = cur.next.next
            cur.next.next.next = temp
            cur = cur.next.next
        return dummy.next


