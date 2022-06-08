# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。 
# 
#  你可以认为每种硬币的数量是无限的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1 
# 
#  示例 2： 
# 
#  
# 输入：coins = [2], amount = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：coins = [1], amount = 0
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：coins = [1], amount = 1
# 输出：1
#  
# 
#  示例 5： 
# 
#  
# 输入：coins = [1], amount = 2
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 231 - 1 
#  0 <= amount <= 104 
#  
#  Related Topics 动态规划 
#  👍 1107 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
这里需要注意的是，"+1"是因为例如当前目标值为10，那么目标值为5时已经计算过需要的最少货币数，
那么从5到10中间需要最少一枚5元硬币即可，所以总的是目标值为5的货币数再加上一枚5元货币数即可。
"""
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [[0] + [amount+1] * amount for _ in range(len(coins)+1)]
#         for i in range(1, len(coins)+1):
#             for aim in range(1, amount+1):
#                 if aim - coins[i-1] >= 0:
#                     dp[i][aim] = min(dp[i-1][aim], dp[i][aim-coins[i-1]]+1)
#                 else:
#                     dp[i][aim] = dp[i-1][aim]
#         return dp[len(coins)][amount] if not dp[len(coins)][amount] == amount+1 else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount+1] * amount
        for coin in coins:
            for aim in range(coin, amount+1):
                dp[aim] = min(dp[aim], dp[aim-coin] + 1)
        return dp[amount] if not dp[amount]==amount+1 else -1
# leetcode submit region end(Prohibit modification and deletion)
