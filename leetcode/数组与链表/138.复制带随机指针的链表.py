"""
https://leetcode.cn/problems/copy-list-with-random-pointer/
解题思路：https://leetcode.cn/problems/copy-list-with-random-pointer/solution/tong-su-li-jie-by-xiao-fu-de-fu-kqs6/
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # 方法一
    def copyRandomList1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        maps = dict()
        p = head
        while p:
            maps[p] = Node(p.val)
            p = p.next
        p = head
        while p:
            if p.next:
                nextnode = maps[p.next]
            else:
                nextnode = None
            if not p.random:
                randomnode = None
            else:
                randomnode = maps[p.random]
            node = maps[p]
            node.next = nextnode
            node.random = randomnode
            p = p.next
        return maps[head]

    # 方法二
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        p = head
        while p:
            temp = p.next
            copy = Node(p.val)
            p.next = copy
            copy.next = temp
            p = temp
        p = head
        while p and p.next:
            if p.random:
                copyrandom = p.random.next
            else:
                copyrandom = None
            p.next.random = copyrandom
            p = p.next.next
        dummy = Node(0)
        dummy.next = head.next
        p = dummy.next
        while p and p.next:
            node = p.next.next
            p.next = node
            p = node
        return dummy.next