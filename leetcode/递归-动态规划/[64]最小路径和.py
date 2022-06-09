# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。 
# 
#  说明：每次只能向下或者向右移动一步。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 200 
#  0 <= grid[i][j] <= 100 
#  
#  Related Topics 数组 动态规划 
#  👍 810 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
动态规划：二维数组
T: O(mn)
S: O(mn)
"""
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         dp = grid
#         r, c = len(grid), len(grid[0])
#         for i in range(1, c):
#             dp[0][i] += dp[0][i-1]
#         for i in range(1, r):
#             dp[i][0] += dp[i-1][0]
#         for i in range(1, r):
#             for j in range(1, c):
#                 dp[i][j] += min(dp[i-1][j], dp[i][j-1])
#         return dp[r-1][c-1]

"""
动态规划：一维数组
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp, r, c = grid[0][:], len(grid), len(grid[0])
        for i in range(1, c):
            dp[i] += dp[i-1]
        for i in range(1, r):
            dp[0] += grid[i][0]
            for j in range(1, c):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
