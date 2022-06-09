# 给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。 
# 
#  
# 
#  示例： 
# 
#  输入: root = [4,2,6,1,3,null,null]
# 输出: 1
# 解释:
# 注意，root是树节点对象(TreeNode object)，而不是数组。
# 
# 给定的树 [4,2,6,1,3,null,null] 可表示为下图:
# 
#           4
#         /   \
#       2      6
#      / \    
#     1   3
# 
# 最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。 
# 
#  
# 
#  注意： 
# 
#  
#  二叉树的大小范围在 2 到 100。 
#  二叉树总是有效的，每个节点的值都是整数，且不重复。 
#  本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/ 
# 相同 
#  
#  Related Topics 树 递归 
#  👍 104 👎 0
"""
该题特别容易忽略题目中"任意"二字，会造成想到中序遍历方法后，疑惑于相邻节点中左子树最右节点与根节点并非
原二叉树中相邻接点。

搜索二叉树出现，首先想到中序遍历。搜索二叉树的中序遍历结果是节点值按升序排列。
（1）先按中序遍历将二叉树节点值升序排列，每个节点值压入栈中
（2）依次计算栈中两两相邻元素的差值，并返回最终差值中的最小值即可

其实也可以不用栈，直接在中序遍历中保留差值的最小值就行：
T: O(N)
S: O(H)

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.min_diff = 1e16
        self.pre = None
        def inorder(node):
            if not node: return
            inorder(node.left)
            if self.pre:
                self.min_diff = min(self.min_diff, node.val - self.pre)
            self.pre = node.val
            inorder(node.right)
        inorder(root)
        return self.min_diff

"""

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
T: O(N)
S: O(N)
"""
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.order = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            if node:
                self.order.append(node.val)
            inorder(node.right)
        inorder(root)
        min_diff = 1e16
        for i in range(1, len(self.order)):
            min_diff = min(min_diff, self.order[i] - self.order[i-1])
        return min_diff
# leetcode submit region end(Prohibit modification and deletion)
