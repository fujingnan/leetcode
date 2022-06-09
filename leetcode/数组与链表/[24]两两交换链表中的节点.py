# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 100] 内 
#  0 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：你能在不修改链表节点值的情况下解决这个问题吗?（也就是说，仅修改节点本身。） 
#  Related Topics 递归 链表 
#  👍 838 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
迭代法
"""
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if not head: return head
#         p = ListNode(0)
#         p.next = head
#         cur = p
#         while cur.next and cur.next.next:
#             first, second = cur.next, cur.next.next
#             cur.next = second
#             first.next = second.next
#             second.next = first
#             cur = first
#         return p.next
"""
递归
T: O(N)
S: O(N)
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        node = head.next
        head.next = self.swapPairs(node.next)
        node.next = head
        return node
# leetcode submit region end(Prohibit modification and deletion)
