# 给你一个 m * n 的整数矩阵 mat ，请你将同一条对角线上的元素（从左上到右下）按升序排序后，返回排好序的矩阵。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# 输出：[[1,1,1,1],[1,2,2,2],[1,2,3,3]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length
#  n == mat[i].length
#  1 <= m, n <= 100 
#  1 <= mat[i][j] <= 100 
#  
#  Related Topics 基础排序 数组
#  👍 29 👎 0

# leetcode submit region begin(Prohibit modification and deletion)
"""
T: O(row*col*log(min(m,n)))
s: O(row*col)
"""
# class Solution:
#     def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
#         row, col = len(mat), len(mat[0])
#         if row == col == 1:
#             return mat
#         diag = {}
#         for i in range(row):
#             for j in range(col):
#                 diag.setdefault(i-j, []).append(mat[i][j])
#         diag = {k: sorted(v, reverse=True) for k, v in diag.items()}
#         for i in range(row):
#             for j in range(col):
#                 mat[i][j] = diag[i-j].pop()
#         return mat
"""
T: O(row*col*log(min(row, col)))
S: O(min(row, col))
"""
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        def sortOne(i, j):
            diags = []
            while i < row and j < col:
                diags.append(mat[i][j])
                i += 1
                j += 1
            diags.sort()
            while i > 0 and j > 0:
                i -= 1
                j -= 1
                mat[i][j] = diags.pop()
        for i in range(row): sortOne(i, 0)
        for j in range(1, col): sortOne(0, j)
        return mat
# leetcode submit region end(Prohibit modification and deletion)
