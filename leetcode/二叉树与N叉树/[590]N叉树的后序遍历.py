# 给定一个 N 叉树，返回其节点值的后序遍历。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其后序遍历: [5,6,3,2,4,1]. 
# 
#  
# 
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树 
#  👍 122 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
"""
递归法
"""
# class Solution:
#     def __init__(self):
#         self.res = []
#     def postorder(self, root: 'Node') -> List[int]:
#         if not root: return
#         for node in root.children:
#             self.postorder(node)
#         self.res.append(root.val)
#         return self.res
"""
迭代法
"""
# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         if not root: return []
#         helper, stack = [], [root]
#         while stack:
#             root = stack.pop()
#             if root:
#                 helper.append(root.val)
#             for node in root.children:
#                 stack.append(node)
#         while helper:
#             stack.append(helper.pop())
#         return stack
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        helper, stack = [], [root]
        while stack:
            root = stack.pop()
            helper.append(root.val)
            stack.extend(root.children)
        while helper:
            stack.append(helper.pop())
        return stack
# leetcode submit region end(Prohibit modification and deletion)
