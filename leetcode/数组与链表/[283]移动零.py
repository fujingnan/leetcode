# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  示例: 
# 
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0] 
# 
#  说明: 
# 
#  
#  必须在原数组上操作，不能拷贝额外的数组。 
#  尽量减少操作次数。 
#  
#  Related Topics 数组 双指针 
#  👍 955 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
常规解法：遍历数组，遇到不为零的数，如果前一位置的数为零，就与前一位置的数交换位置
"""
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if len(nums) == 1: return nums
#         for i, n in enumerate(nums):
#             if i and n:
#                 while i and not nums[i-1]:
#                     nums[i], nums[i-1] = nums[i-1], nums[i]
#                     i -= 1
#         return nums
"""
双指针
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
# leetcode submit region end(Prohibit modification and deletion)
