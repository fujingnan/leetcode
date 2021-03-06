# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  注意：给定 n 是一个正整数。 
# 
#  示例 1： 
# 
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶 
# 
#  示例 2： 
# 
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#  
#  Related Topics 动态规划 
#  👍 1476 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
动态规划i
T: O(N)
S: O(N)
"""
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n < 2: return n
#         dp = [0 for _ in range(n)]
#         dp[0], dp[1] = 1, 2
#         for i in range(2, n):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[-1]
"""
动态规划ii
T: O(N)
S: O(1)
"""
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n < 2: return n
#         a, b = 1, 2
#         for i in range(2, n):
#             a, b = b, a + b
#         return b
"""
直接递归法
"""
class Solution:
    @functools.lru_cache(100)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)
# leetcode submit region end(Prohibit modification and deletion)
