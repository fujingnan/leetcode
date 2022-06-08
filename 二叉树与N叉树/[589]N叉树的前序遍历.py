# 给定一个 N 叉树，返回其节点值的前序遍历。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其前序遍历: [1,3,5,6,2,4]。 
# 
#  
# 
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树 
#  👍 129 👎 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
"""迭代法"""
# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         if not root: return []
#         helper, res = [], [root]
#         while res:
#             root = res.pop()
#             helper.append(root.val)
#             res.extend(root.children[::-1])
#         return helper
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res, stack = [], root and [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            stack += [child for child in root.children[::-1]]
        return res
"""递归法"""
# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         res = []
#         def dfs(root):
#             if not root: return []
#             res.append(root.val)
#             for node in root.children:
#                 dfs(node)
#         dfs(root)
#         return res
# leetcode submit region end(Prohibit modification and deletion)
