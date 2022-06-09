# 数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。 
# 
#  每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。 
# 
#  您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。 
# 
#  示例 1: 
# 
#  输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
#  
# 
#  示例 2: 
# 
#  输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
# 
# 
#  注意： 
# 
#  
#  cost 的长度将会在 [2, 1000]。 
#  每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。 
#  
#  Related Topics 数组 动态规划
#  👍 409 👎 0
"""
# f(i) = min(f(i-1)+cost(i-1), f(i-2)+cost(i-2))
初看题意，利用动态规划方法时容易陷入一个误区：计算 dp[i] 时，即算第 i 个台阶的值，实际上是
在计算到达第 i+1 个台阶需要花费的体力，而不是计算到达第 i 个台阶花费的体力。因此当遍历到 i
时，dp[i]有两个来源：
（1）脚从 i-1 来，越过 i，直接到达第 i+1 个台阶，既然脚从 i-1 来，则花费值为 dp[i-1] +
cost[i-1]，即 dp[i]=dp[i-1]+cost[i-1]
（2）脚从 i-2 来，到达 i，再到达第 i+1 个台阶，既然脚从 i-2 来，则花费值为 dp[i-2] +
cost[i-2]，即 dp[i]=dp[i-2]+cost[i-2]
（3）需要注意的是，不管是第一种情况还是第二种情况，在经过 i 的时候，都没有计算第 i 个台阶的
体力花费值，因为 i 的值只和下一个或者下下个台阶有关，因此综合（1）（2），

            dp[i]=min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

该式即为动态规划状态转移方程
"""

"""
T: O(N)
S: O(N)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not len(cost): return 0
        min_cost = [0 for _ in range(len(cost)+1)]
        min_cost[0], min_cost[1] = 0, min(min_cost[0], min_cost[1])
        for i in range(2, len(cost)+1):
            min_cost[i] = min(min_cost[i-1]+cost[i-1], min_cost[i-2]+cost[i-2])
        return min_cost[-1]
"""
"""
该题也可以直接在原数组上操作，这个时候，当遍历到 i 的时候，cost[i] 无非有两种情况：
（1）第 i-1 个台阶所花费的体力与第 i 个台阶所花费的体力之和，cost[i]=cost[i-1]+cost[i]
（2）第 i-2 个台阶所花费的体力与第 i 个台阶所花费的体力之和，cost[i]=cost[i-2]+cost[i]
（3）那么综合（1）（2）：
    cost[i]=min(cost[i-1]+cost[i], cost[i-2]+cost[i])=min(cost[i-1], cost[i-2])+cost[i]
    
T: O(N)
S: O(1)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 2], cost[i - 1]) + cost[i]
        return min(cost[-2], cost[-1])

"""


# leetcode submit region begin(Prohibit modification and deletion)
"""
T: O(N)
S: O(1)
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not len(cost): return 0
        # min_cost = [0 for _ in range(len(cost)+1)]
        min_pre = temp = 0
        min_cur = min(min_pre, cost[0])
        for i in range(2, len(cost)+1):
            temp = min_cur
            min_cur = min(min_cur+cost[i-1], min_pre+cost[i-2])
            min_pre = temp
        return min_cur

# leetcode submit region end(Prohibit modification and deletion)
