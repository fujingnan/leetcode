# 给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。 
# 
#  示例: 
# 
#  输入: matrix = [[1,0,1],[0,-2,3]], k = 2
# 输出: 2 
# 解释: 矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
#  
# 
#  说明： 
# 
#  
#  矩阵内的矩形区域面积必须大于 0。 
#  如果行数远大于列数，你将如何解答呢？ 
#  
#  Related Topics 队列 二分查找 动态规划 
#  👍 166 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        max_sum = -float('inf')
        for left in range(col):
            row_sum = [0] * row
            for right in range(left, col):
                for r in range(row):
                    row_sum[r] += matrix[r][right]
                max_sum = max(max_sum, self.find_m(row_sum, k))
                if max_sum == k:
                    return k
        return max_sum

    def find_m(self, arr, k):
        n = len(arr)
        sum, dp = -float('inf'), [0] * n
        for i in range(n):
            dp[i] = max(arr[i], dp[i - 1] + arr[i])
            if dp[i] > sum:
                sum = dp[i]
        if sum <= k:
            return sum
        max_sum, sum = -float('inf'), 0
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += arr[j]
                if sum <= k:
                    max_sum = max(max_sum, sum)
                    if max_sum == k:
                        return k
        return max_sum
# leetcode submit region end(Prohibit modification and deletion)
