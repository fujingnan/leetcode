# 三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。
# 
#  示例1: 
# 
#  
#  输入：n = 3 
#  输出：4
#  说明: 有四种走法
#  
# 
#  示例2: 
# 
#  
#  输入：n = 5
#  输出：13
#  
# 
#  提示: 
# 
#  
#  n范围在[1, 1000000]之间 
#  
#  Related Topics 动态规划 
#  👍 34 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
T: O(N)
S: O(N)
"""
# class Solution:
#     def waysToStep(self, n: int) -> int:
#         if n < 3: return n
#         ways = [0] * n
#         ways[0], ways[1], ways[2] = 1, 2, 4
#         for i in range(3, n):
#             ways[i] = (ways[i-1] + ways[i-2] + ways[i-3]) % 1000000007
#         return ways[-1]
"""
T: O(N)
S: O(1)
"""
class Solution:
    def waysToStep(self, n: int) -> int:
        if n < 3: return n
        first, second, third = 1, 2, 4
        for i in range(3, n):
            first, second, third = second, third, (first + second + third) % 1000000007
        return third

"""
利用滚动数组的思想
T: O(N)
S: O(1)
"""
# class Solution:
#     def waysToStep(self, n: int) -> int:
#         if n < 3: return n
#         dp = [1, 2, 4]
#         for i in range(3, n):
#             dp[i % 3] = (dp[(i-3) % 3] + dp[(i-1) % 3] + dp[(i-2) % 3]) % 1000000007
#         return dp[(n-1) % 3]
# leetcode submit region end(Prohibit modification and deletion)
