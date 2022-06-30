"""
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
解题思路：https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solution/zui-rong-yi-li-jie-de-by-xiao-fu-de-fu-vru2/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        slow = dummy
        fast = head
        n -= 1
        while n:
            fast = fast.next
            n -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        temp = slow.next.next
        slow.next.next = None
        slow.next = temp
        return dummy.next