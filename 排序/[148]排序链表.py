# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 
# 
#  进阶： 
# 
#  
#  你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 5 * 104] 内
#  -105 <= Node.val <= 105 
#  
#  Related Topics 排序 链表 
#  👍 942 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
迭代法：
T: O(N*logN)
S: O(1)
"""
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         size = 0
#         p = head
#         while p:
#             size += 1
#             p = p.next
#         def cutLink(h, step):
#             if not h: return None
#             cur = ListNode(0)
#             cur.next = h
#             cur = cur.next
#             while cur.next and step-1:
#                 cur = cur.next
#                 step -= 1
#             resLink = ListNode(0)
#             resLink.next = cur.next
#             cur.next = None
#             return resLink.next
#         def merge(h1, h2):
#             dummy = ListNode(0)
#             cur = dummy
#             while h1 and h2:
#                 if h1.val < h2.val:
#                     cur.next = h1
#                     h1 = h1.next
#                 else:
#                     cur.next = h2
#                     h2 = h2.next
#                 cur = cur.next
#             if h1:
#                 cur.next = h1
#             if h2:
#                 cur.next = h2
#             return dummy.next
#         dummy = ListNode(0)
#         dummy.next = head
#         step = 1
#         while step < size:
#             fast, slow = dummy.next, dummy
#             while fast:
#                 h1 = fast
#                 h2 = cutLink(h1, step)
#                 fast = cutLink(h2, step)
#                 sub_merge = merge(h1, h2)
#                 slow.next = sub_merge
#                 while slow.next:
#                     slow = slow.next
#             step *= 2
#         return dummy.next
"""
递归法：
T: O(N*logN)
S: O(logN)
"""
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         if not head or not head.next: return head
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow, fast = slow.next, fast.next.next
#         mid, slow.next = slow.next, None
#         left = self.sortList(head)
#         right = self.sortList(mid)
#         dummy = ListNode(0)
#         cur = dummy
#         while left and right:
#             if left.val < right.val:
#                 cur.next = left
#                 left = left.next
#             else:
#                 cur.next = right
#                 right = right.next
#             cur = cur.next
#         if left: cur.next = left
#         if right: cur.next = right
#         return dummy.next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        while h: h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h: h, i = h.next, i - 1
                if i: break # no need to merge because the `h2` is None.
                h2, i = h, intv
                while i and h: h, i = h.next, i - 1
                c1, c2 = intv, intv - i # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val: pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else: pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            intv *= 2
        return res.next
# leetcode submit region end(Prohibit modification and deletion)
