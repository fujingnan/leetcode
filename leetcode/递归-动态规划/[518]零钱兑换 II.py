# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
# 
#  
# 
#  
#  
# 
#  示例 1: 
# 
#  输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#  
# 
#  示例 2: 
# 
#  输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
#  
# 
#  示例 3: 
# 
#  输入: amount = 10, coins = [10] 
# 输出: 1
#  
# 
#  
# 
#  注意: 
# 
#  你可以假设： 
# 
#  
#  0 <= amount (总金额) <= 5000 
#  1 <= coin (硬币面额) <= 5000 
#  硬币种类不超过 500 种 
#  结果符合 32 位符号整数 
#  
#  👍 335 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         if not coins and not amount: return 1
#         if not coins and amount: return 0
#         dp = [[1] + [0] * amount for _ in range(len(coins))]
#         for j in range(1, amount+1):
#             if j * coins[0] <= amount:
#                 dp[0][j * coins[0]] = 1
#         for i in range(1, len(coins)):
#             for j in range(1, amount+1):
#                 dp[i][j] = dp[i-1][j]
#                 dp[i][j] += dp[i][j-coins[i]] if j-coins[i] >= 0 else 0
#         return dp[len(coins)-1][amount]
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not coins and not amount: return 1
        if not coins and amount: return 0
        dp = [1] + [0] * (amount)
        for j in range(1, amount+1):
            if j * coins[0] <= amount:
                dp[j * coins[0]] = 1
        for i in range(1, len(coins)):
            for j in range(1, amount+1):
                dp[j] += dp[j-coins[i]] if j-coins[i] >= 0 else 0
        return dp[amount]

# leetcode submit region end(Prohibit modification and deletion)
