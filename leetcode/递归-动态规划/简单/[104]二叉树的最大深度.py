# 给定一个二叉树，找出其最大深度。 
# 
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例： 
# 给定二叉树 [3,9,20,null,null,15,7]， 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回它的最大深度 3 。 
#  Related Topics 树 深度优先搜索 递归 
#  👍 749 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
DFS: T: O(N)
     S: O(N)
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        stack, curMax = [(root, 1)], 0
        while stack:
            node, dep = stack.pop(-1)
            curMax = max(curMax, dep)
            if node.right: stack.append((node.right, dep+1))
            if node.left: stack.append((node.left, dep+1))
        return curMax
# leetcode submit region end(Prohibit modification and deletion)
