# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。 
# 
#  子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序
# 列。 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2500 
#  -104 <= nums[i] <= 104 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你可以设计时间复杂度为 O(n2) 的解决方案吗？ 
#  你能将算法的时间复杂度降低到 O(n log(n)) 吗? 
#  
#  Related Topics 二分查找 动态规划 
#  👍 1478 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
暴力求解
T: O(N^2)
S: O(N)
"""
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if len(nums) < 2:
#             return 1
#         dp = [1] * len(nums)
#         for i in range(1, len(nums)):
#             maxn = 0
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     maxn = max(maxn, dp[j])
#                 dp[i] = maxn + 1
#         return max(dp)
"""
构建单调栈-二分法迭代版：
T：O（NlogN）
S：O（N）
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 1
        size = len(nums)
        ends = [nums[0]]
        for i in range(1, size):
            if nums[i] > ends[-1]:
                ends.append(nums[i])
                continue
            left, right, mid = 0, len(ends) - 1, 0
            while left < right:
                mid = (right + left) >> 1
                if nums[i] <= ends[mid]:
                    right = mid
                else:
                    left = mid + 1
            ends[right] = nums[i]
        return len(ends)
"""
构建单调栈-二分法递归版(递归开销空间，非最优)：
T：O（NlogN）
S：O（N）
"""
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if len(nums) < 2:
#             return 1
#         size = len(nums)
#         ends = [nums[0]]
#         for i in range(1, size):
#             if nums[i] > ends[-1]:
#                 ends.append(nums[i])
#                 continue
#             right = self.binary_compare(ends, 0, len(ends)-1, nums[i])
#             ends[right] = nums[i]
#         return len(ends)
#     def binary_compare(self, arr, left, right, target):
#         if left == right:
#             return right
#         mid = (right + left) >> 1
#         if target > arr[mid]:
#             return self.binary_compare(arr, mid + 1, right, target)
#         else:
#             return self.binary_compare(arr, left, mid, target)
# leetcode submit region end(Prohibit modification and deletion)
