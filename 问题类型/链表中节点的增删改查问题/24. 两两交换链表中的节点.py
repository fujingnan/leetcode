"""
https://leetcode.cn/problems/swap-nodes-in-pairs/
解题思路：https://leetcode.cn/problems/swap-nodes-in-pairs/solution/zhu-by-xiao-fu-de-fu-haue/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        dummy = ListNode(None)
        dummy.next = head
        p = dummy.next
        # 为了保证交换后的链表能和后续链表链接起来，所以需要定义一个连接节点始终指向待交换的链表
        prev = dummy
        while p and p.next:
            # 记录下一轮待交换链表的头结点
            temp1 = p.next.next
            # 记录本轮待交换链表的第二个节点
            temp2 = p.next
            # 断开本轮链表和下一轮链表，让本轮链表的第二个节点指向第一个节点
            p.next.next = p
            # 让第一个节点指向下一轮待交换的链表
            p.next = temp1
            # 让连接节点指向第二个节点（交换后为第一个节点）
            prev.next = temp2
            # 连接节点移动到原第一个节点（交换后为下一轮待交换链表的前一个节点）
            prev = p
            # 原第一个节点移动到下一轮待交换链表的第一个节点，完成本轮交换，准备下一轮交换
            p = temp1
        return dummy.next


