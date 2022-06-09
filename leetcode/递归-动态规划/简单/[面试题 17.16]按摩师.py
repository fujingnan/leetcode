# 一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩
# 师找到最优的预约集合（总预约时间最长），返回总的分钟数。 
# 
#  注意：本题相对原题稍作改动 
# 
#  
# 
#  示例 1： 
# 
#  输入： [1,2,3,1]
# 输出： 4
# 解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
#  
# 
#  示例 2： 
# 
#  输入： [2,7,9,3,1]
# 输出： 12
# 解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
#  
# 
#  示例 3： 
# 
#  输入： [2,1,4,5,3,1,1,3]
# 输出： 12
# 解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。
#  
#  Related Topics 动态规划
#  👍 154 👎 0
"""
动态规划：
（1）第0个位置，dp[0]=nums[0]，第一个位置，dp[1]=max(nums[0], nums[1]+nums[1-2])
（2）第i个位置，dp[i]=max(dp[i-1], dp[i-2]+nums[i])。解释：由于第i位置存储的最大值
    要么是不相邻的前一个dp所存储的值（最大值）与当前值得和，要么是上一个相邻dp所存储的值（
    最大值），取这两种情况中较大的值存储在当前dp中
T: O(N)
S: O(N)
"""
# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def massage(self, nums: List[int]) -> int:
#         if not nums: return 0
#         if len(nums) <= 2: return max(nums)
#         best = [0] * len(nums)
#         best[0], best[1] = nums[0], max(nums[0], nums[1])
#         for i in range(2, len(nums)):
#             best[i] = max(best[i-1], best[i-2]+nums[i])
#         return best[-1]
"""
优化空间：不再另外开辟数组空间dp，而是在原数组中操作，利用原数组来存储上述逻辑中的最大值：
T: O(N)
S: O(1)
"""
class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1], nums[i-2]+nums[i])
        return nums[-1]
# leetcode submit region end(Prohibit modification and deletion)
