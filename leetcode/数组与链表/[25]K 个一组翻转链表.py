# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。 
# 
#  k 是一个正整数，它的值小于或等于链表的长度。 
# 
#  如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。 
# 
#  进阶： 
# 
#  
#  你可以设计一个只使用常数额外空间的算法来解决此问题吗？ 
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1,2,3,4,5], k = 1
# 输出：[1,2,3,4,5]
#  
# 
#  示例 4： 
# 
#  
# 输入：head = [1], k = 1
# 输出：[1]
#  
# 
#  
#  
# 
#  提示： 
# 
#  
#  列表中节点的数量在范围 sz 内 
#  1 <= sz <= 5000 
#  0 <= Node.val <= 1000 
#  1 <= k <= sz 
#  
#  Related Topics 链表 
#  👍 936 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
利用栈
T: O(N)
S: O(1)
"""
# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         if not head or k <= 1:
#             return head
#         reverse= ListNode(0)
#         cur = reverse
#         stack = []
#         while head:
#             stack.append(head.val)
#             if len(stack) == k:
#                 while stack:
#                     cur.next = ListNode(stack.pop())
#                     cur = cur.next
#             head = head.next
#         for i in stack:
#             cur.next = ListNode(i)
#             cur = cur.next
#         return reverse.next

"""
迭代法
T: O(N)
S: O(1)
"""
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k <= 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        start, end = dummy, head
        count = 0
        while end:
            count += 1
            if count % k == 0:
                start = self.reverse1Group(start, end.next)
                end = start.next
            else:
                end = end.next
        return dummy.next
    def reverse1Group(self, left, right):
        prev = left
        head = left.next
        cur = head
        while not cur == right:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        left.next = prev
        head.next = cur
        return head
# leetcode submit region end(Prohibit modification and deletion)
