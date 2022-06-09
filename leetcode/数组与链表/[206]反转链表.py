# 反转一个单链表。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL 
# 
#  进阶: 
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？ 
#  Related Topics 链表 
#  👍 1549 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
重建链表
T：O(N)
S: O(N)
"""
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head:
#             return head
#         stack, reverse = [], ListNode(0)
#         while head:
#             stack.append(head.val)
#             head = head.next
#         cur = reverse
#         while stack:
#             v = stack.pop()
#             cur.next = ListNode(v)
#             cur = cur.next
#         return reverse.next
"""
迭代法
T: O(N)
S: O(1)
"""
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head:
#             return head
#         cur, prev = head, None
#         while cur:
#             tempNode = cur.next
#             cur.next = prev
#             prev = cur
#             cur = tempNode
#         return prev
"""
递归
T: O(N)
S: O(N)
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur
# leetcode submit region end(Prohibit modification and deletion)
