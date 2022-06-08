# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
# 
#  现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？ 
# 
#  
# 
#  网格中的障碍物和空位置分别用 1 和 0 来表示。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#  
# 
#  示例 2： 
# 
#  
# 输入：obstacleGrid = [[0,1],[0,0]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == obstacleGrid.length 
#  n == obstacleGrid[i].length 
#  1 <= m, n <= 100 
#  obstacleGrid[i][j] 为 0 或 1 
#  
#  Related Topics 数组 动态规划 
#  👍 505 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
动态规划：本题和 https://leetcode-cn.com/problems/unique-paths/submissions/ 一样的，
但是需要注意的是，由于本题设置了障碍物，所以每一个格子的走法都有可能为0，所以dp的初始化必须是第
一个位置为1，其余位置必须为0，如果为1，说明默认每一个格子至少有一种走法，这不符合可能有障碍物的条
件，既然初始化只有第一个位置为1，所以i，j的遍历都必须从0位置开始，否则后面都为0，就累加也是0，出错。
既然从0位置开始遍历，那么最终状态就是倒数第二个位置。
T：O（mn）
S：O（n）
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [1] + [0] * n
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                else:
                    dp[j] += dp[j-1]
        print(dp)
        return dp[-2]
# leetcode submit region end(Prohibit modification and deletion)
