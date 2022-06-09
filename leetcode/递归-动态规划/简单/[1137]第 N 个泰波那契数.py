# 泰波那契序列 Tn 定义如下： 
# 
#  T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2 
# 
#  给你整数 n，请返回第 n 个泰波那契数 Tn 的值。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 4
# 输出：4
# 解释：
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#  
# 
#  示例 2： 
# 
#  输入：n = 25
# 输出：1389537
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 37 
#  答案保证是一个 32 位整数，即 answer <= 2^31 - 1。 
#  
#  Related Topics 递归 
#  👍 53 👎 0
"""
该题需要注意的是，n 是从 0 开始的，因此 n==x 时，实际上序列的长度为 x+1
有一个非常巧妙的解法：
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(3, n+1):
            dp[i % 3] = sum(dp)
        return dp[i % 3]
"""

# leetcode submit region begin(Prohibit modification and deletion)
"""
T: O(N)
S: O(1)
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        if n < 3: return 1 if n else 0
        for _ in range(n-2):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        return t2
        
# leetcode submit region end(Prohibit modification and deletion)
