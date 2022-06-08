# 给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。 
# 
#  
# 
#  示例 ： 
# 
#  输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]
# 
#        5
#       / \
#      3   6
#     / \   \
#    2   4   8
#   /       / \
#  1       7   9
#
# 遍历结果：[1,2,null,3,4,5,null,6,7,8,9]
# 
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# 
#  1
#   \
#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6
#             \
#              7
#               \
#                8
#                 \
#                  9
# 
#  
# 
#  提示： 
# 
#  
#  给定树中的结点数介于 1 和 100 之间。 
#  每个结点都有一个从 0 到 1000 范围内的唯一整数值。 
#  
#  Related Topics 树 深度优先搜索 递归 
#  👍 120 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
先在树上进行中序遍历，当我们遍历到一个节点时，把它的左孩子设为空，并将其本身作为上一个遍历到的节点的右孩子

T：O(N)
S：O(H)
"""
class Solution:
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root: return None
        def inorder(node):
            if not node: return
            inorder(node.left)
            node.left = None
            self.cur.right = node
            self.cur = node
            inorder(node.right)
        head = TreeNode(None)
        self.cur = head
        inorder(root)
        return head.right
"""
    def increasingBST(self, root, tail = None):
        if not root: return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res
"""

# leetcode submit region end(Prohibit modification and deletion)
