# 给定一个二叉树，返回它的 后序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 
# 
# 输出: [3,2,1] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 
#  👍 506 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
递归法
"""
# class Solution:
#     def __init__(self):
#         self.res = []
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root: return []
#         self.postorderTraversal(root.left)
#         self.postorderTraversal(root.right)
#         self.res.append(root.val)
#         return self.res
"""
迭代法一：利用双栈
"""
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root: return []
#         s1, s2, res = [root], [], []
#         while s1:
#             root = s1.pop()
#             s2.append(root.val)
#             if root.left:
#                 s1.append(root.left)
#             if root.right:
#                 s1.append(root.right)
#         while s2:
#             res.append(s2.pop())
#         return res
"""
迭代法二：利用单栈(morris遍历)
"""
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, stack, head, cur = [], [root], root, None
        while stack:
            cur = stack[-1]
            if cur.left and not (cur.left == head or cur.right == head):
                stack.append(cur.left)
            elif cur.right and not cur.right == head:
                stack.append(cur.right)
            else:
                head = stack.pop()
                res.append(head.val)
        return res
# leetcode submit region end(Prohibit modification and deletion)
