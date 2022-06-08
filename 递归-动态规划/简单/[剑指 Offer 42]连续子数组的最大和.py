# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。 
# 
#  要求时间复杂度为O(n)。 
# 
#  
# 
#  示例1: 
# 
#  输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^5 
#  -100 <= arr[i] <= 100
#  
# 
#  注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/ 
# 
#  
#  Related Topics 分治算法 动态规划 
#  👍 175 👎 0

"""
利用动态规划，在原数组上操作即可：遍历数组，初始时，记录数组第一个位置的值，从数组的第二个位置开始，
后面数组的每个位置的值与数组前一位置值相加，并与当前值作比较，保留二者最大，并记录在数组当前位置。

                nums[i] = max(nums[i], nums[i] + nums[i-1])

    例：
                   0 [-2, 1, -3, 4, -1, 2, 1, -5, 4]
                      0,  1, -2, 4,  3, 5, 6,  1, 5
                                           ^
"""
# leetcode submit region begin(Prohibit modification and deletion)
"""
T:O(N)
S:O(1)
"""
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if len(nums) == 1: return nums[0]
#         nums[0] = max(-float('inf'), nums[0])
#         for i in range(1, len(nums)):
#             nums[i] = max(nums[i], nums[i] + nums[i-1])
#         return max(nums)
"""
也可利用两个变量 pre 和 max_sum 完成：遍历数组，当前值加上前面子数组计算的和如果呈现减小的情况，
那么当前值一定不在连续最大子数组中
"""
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if len(nums) == 1: return nums[0]
#         max_sum, pre = -float('inf'), 0
#         for cur in nums:
#             pre = max(cur, pre + cur)
#             max_sum = max(max_sum, pre)
#         return max_sum

"""
利用两个变量sum和max_sum。遍历数组，累加遍历值，当累加和为负，累加和置为0，这是因为一个数组中，只
要存在正值，那么该数组最大连续子数组之和都不可能为负，最差只有一个正数，则该数组最大连续子数组和即为
该正数。如果整个数组都为负，那么max_sum只记录最大的sum值即可，因为max_sum值的计算在sum置为0之前，
所以不受影响
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        max_sum, sum = -float('inf'), 0
        for cur in nums:
            sum += cur
            max_sum = max(max_sum, sum)
            if sum < 0: sum = 0
        return max_sum
# leetcode submit region end(Prohibit modification and deletion)
