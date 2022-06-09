# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [["0"]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 300 
#  matrix[i][j] 为 '0' 或 '1' 
#  
#  Related Topics 动态规划 
#  👍 715 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         row, col, maxS = len(matrix), len(matrix[0]), 0
#         dp = [[0] * col for _ in range(row)]
#         for i in range(row):
#             for j in range(col):
#                 if matrix[i][j] == '1':
#                     if not i or not j:
#                         dp[i][j] = 1
#                     else:
#                         dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
#                 maxS = max(maxS, dp[i][j])
#         return maxS * maxS

# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         row, col = len(matrix), len(matrix[0])
#         dp = [int(i) for i in matrix[0]]
#         pre, maxside = 0, 1 if 1 in dp else 0
#         for i in range(1, row):
#             pre = dp[0] # 左上角的值
#             if matrix[i][0] == '1':
#                 dp[0] = 1 # 左边的值
#             else:
#                 dp[0] = 0 # 左边的值
#             maxside = max(maxside, dp[0])
#             for j in range(1, col):
#                 if matrix[i][j] == '1':
#                     cur = dp[j] # 上面的值
#                     dp[j] = min(cur, dp[j-1], pre) + 1
#                     pre = cur
#                 else:
#                     pre = dp[j]
#                     dp[j] = 0
#                 maxside = max(maxside, dp[j])
#         return maxside * maxside

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [0] * (col + 1)
        maxside = 0
        for i in range(row):
            pre = 0
            for j in range(1, col+1):
                if matrix[i][j-1] == '1':
                    cur = dp[j] # 上面的值
                    dp[j] = min(cur, dp[j-1], pre) + 1
                    pre = cur
                else:
                    pre = dp[j]
                    dp[j] = 0
                maxside = max(maxside, dp[j])
        return maxside * maxside

# leetcode submit region end(Prohibit modification and deletion)
