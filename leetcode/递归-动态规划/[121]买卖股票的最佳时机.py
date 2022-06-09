# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。 
# 
#  你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。 
# 
#  返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#  
# 
#  示例 2： 
# 
#  
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 105 
#  0 <= prices[i] <= 104 
#  
#  Related Topics 数组 动态规划 
#  👍 1507 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
设置变量cur与res：cur存储当前买入价格，res存储赚取的最高金额，初始值cur=prices[0]，res=0：
遍历prices从第二个位置开始，如果第二个位置的值小于第一个位置，cur设置成第二个位置值，否则，
cur不变，res等于当前价格减去买入价格（cur）的值与当前res的值取最大，以此类推
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        cur, res = prices[0], 0
        for price in prices[1:]:
            cur = min(price, cur)
            res = max(res, price - cur)
        return res
# leetcode submit region end(Prohibit modification and deletion)
