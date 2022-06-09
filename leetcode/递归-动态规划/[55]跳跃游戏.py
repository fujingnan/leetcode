# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  判断你是否能够到达最后一个下标。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 104 
#  0 <= nums[i] <= 105 
#  
#  Related Topics 贪心算法 数组 
#  👍 1094 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
暴力法：超时
"""
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if nums[0] == len(nums) - 1:
#             return True
#         if len(nums) == 1:
#             return True
#         dp = [['False'] * (len(nums)-1) for _ in nums]
#         for i in range(len(nums)-1, 0, -1):
#             for j in range(i):
#                 if nums[j] >= i - j:
#                     dp[i][j] = 'True'
#                     break
#             if not 'True' in dp[i]:
#                 return False
#         return True
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if nums[0] == len(nums) - 1:
#             return True
#         if len(nums) == 1:
#             return True
#         dp = [False for _ in nums]
#         dp[0] = True
#         for i in range(1, len(nums)):
#             for j in range(i):
#                 if dp[j] and i - j <= nums[j]:
#                     dp[i] = True
#         return dp[-1]
"""
遍历数组，记录下当前数为步长能跳跃的最大距离，并与当前下标对比，如果能跳跃的最大距离能覆盖住当前坐标，
说明能到达终点
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dist = 0
        for i in range(len(nums)):
            if i > dist:
                return False
            dist = max(dist, i + nums[i])
        return True
# leetcode submit region end(Prohibit modification and deletion)
