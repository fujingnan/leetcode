# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [-1]
# 输出：-1
#  
# 
#  示例 5： 
# 
#  
# 输入：nums = [-100000]
# 输出：-100000
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 104 
#  -105 <= nums[i] <= 105 
#  
# 
#  
# 
#  进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。 
#  Related Topics 数组 分治算法 动态规划 
#  👍 2971 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
递推
初始化指针cur以及存储结果的和sum：cur的初始化值为第一个数，从第2个位置开始遍历，每遍历一个数，将当前数与cur
相加，让cur赋值为当前数与当前数加前一个cur之和中较大的数，这样做的意义在于：如果当前数加上前一个数反而变小了，
那么说明新的累加起点应该抛弃前面的数而从当前数开始，否则绝不会出现最大累加和。
"""
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         cur = sum = nums[0]
#         for x in nums[1:]:
#             cur = max(x, cur+x)
#             sum = max(sum, cur)
#         return sum
"""
动态规划
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = nums
        for i in range(1, n):
            dp[i] = max(dp[i], dp[i - 1] + nums[i])
        # exm: [-2,1,-3,4,-1,2,1,-5,4]
        # dp: [-2, 1, -2, 4, 3, 5, 6, 1, 5]
        return max(dp)
# leetcode submit region end(Prohibit modification and deletion)
