# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。 
# 
#  给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。 
# 
#  完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4 
# 
#  示例 2： 
# 
#  
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 104 
#  
#  Related Topics 广度优先搜索 数学 动态规划 
#  👍 799 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
广度优先搜索
"""
class Solution:
    def numSquares(self, n: int) -> int:
        from collections import deque
        q = deque([n])
        s = set()
        s.add(n)
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                cur = q.pop()
                if not cur:
                    return level-1
                for i in range(1, int(cur ** 0.5) + 1):
                    if not cur - i * i in s:
                        q.appendleft(cur - i * i)
                        s.add(cur - i * i)
"""
时间复杂度高
"""
# class Solution:
#     def numSquares(self, n: int) -> int:
#         dp = [0 for _ in range(n + 1)]
#         for i in range(1, n+1):
#             dp[i] = i
#             for j in range(1, int(i**0.5)+1):
#                 if j * j <= i:
#                     dp[i] = min(dp[i], dp[i-j*j] + 1)
#         return dp[n]

"""
用数学原理（不推荐）
"""
# from math import sqrt
# class Solution:
#     def numSquares(self, n):
#         if int(sqrt(n)) ** 2 == n: return 1
#         for j in range(int(sqrt(n)) + 1):
#             if int(sqrt(n - j * j)) ** 2 == n - j * j: return 2
#
#         while n % 4 == 0:
#             n >>= 2
#         if n % 8 == 7: return 4
#         return 3
# leetcode submit region end(Prohibit modification and deletion)
