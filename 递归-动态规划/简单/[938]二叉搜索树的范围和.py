# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
# 输出：32
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# 输出：23
#  
# 
#  
# 
#  提示：
# 
#  
#  树中节点数目在范围 [1, 2 * 104] 内 
#  1 <= Node.val <= 105 
#  1 <= low <= high <= 105 
#  所有 Node.val 互不相同 
#  
#  Related Topics 树 深度优先搜索 递归 
#  👍 146 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
可以中序遍历二叉树，遍历到的节点若位于要求范围之间的，将节点值累加
T: O(N)
S: O(H)
"""
# class Solution:
#     def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
#         self.sum = 0
#         def range_sum(node):
#             if not node: return
#             range_sum(node.left)
#             if node and node.val >= low and node.val <= high:
#                 self.sum += node.val
#             range_sum(node.right)
#         range_sum(root)
#         return self.sum

"""
递归方法，由搜索二叉树的性质：
（1）如果当前节点比范围中的最小值还要小，那么直接递归遍历右子树，结果为右子树所有符合条件节点值之和；
（2）如果当前节点比范围中的最大值还要大，那么直接递归遍历左子树，结果为左子树所有符合条件节点值之和；
（3）如果当前节点位于范围中，那么既要遍历左子树又要遍历右子树，结果为当前节点、右子树、左子树所有符合条件节点值之和；
"""

"""
T: O(N)
S: O(H)
"""
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root: return 0
        if root.val < low: return self.rangeSumBST(root.right, low, high)
        if root.val > high: return self.rangeSumBST(root.left, low, high)

        return root.val+\
               self.rangeSumBST(root.right, low, high)+\
               self.rangeSumBST(root.left, low, high)
# leetcode submit region end(Prohibit modification and deletion)
