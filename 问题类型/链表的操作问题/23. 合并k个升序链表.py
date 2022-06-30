"""
https://leetcode.cn/problems/merge-k-sorted-lists/
解题思路：https://leetcode.cn/problems/merge-k-sorted-lists/solution/he-bing-k-by-xiao-fu-de-fu-uql9/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or (len(lists) == 1 and not lists[0]):
            return None

        def mergeTwolists(h1, h2):
            head = ListNode(None)
            p = head
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
            return head.next

        def merge(lists, left, right):
            if left >= right:
                # 容易错
                return lists[left]
            mid = left + ((right - left) >> 1)
            # 容易漏掉l1和l2
            l1 = merge(lists, left, mid)
            l2 = merge(lists, mid + 1, right)
            return mergeTwolists(l1, l2)

        return merge(lists, 0, len(lists) - 1)