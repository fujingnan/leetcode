# 给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。 
# 
#  示例 1: 
# 
#  输入: nums = [1, 5, 1, 1, 6, 4]
# 输出: 一个可能的答案是 [1, 4, 1, 5, 1, 6] 
# 
#  示例 2: 
# 
#  输入: nums = [1, 3, 2, 2, 3, 1]
# 输出: 一个可能的答案是 [2, 3, 1, 3, 1, 2]
# 
#  说明: 
# 你可以假设所有输入都会得到有效的结果。
# 
#  进阶: 
# 你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？
#  Related Topics 排序
#  👍 222 👎 0

"""
最直接的思路是对数组进行排序，然后均分成左右两个子数组，最后将两数组穿插；为避免[4,5,5,6]这种重复元素
导致的穿插结果无变化的情况，首先需要降序，并将排序后较小的子数组作为被穿插数组，较大的数组作为穿插数组；
T: 长期期望：O(N*logN)
S: O(N)
"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    快速排序
    def quiksort(self, arr, left, right):
        if left >= right: return
        target = arr[(left + right) // 2]
        arr[(left + right) // 2], arr[right] = arr[right], arr[(left + right) // 2]
        r = right
        while left < right:
            while arr[left] >= target and left < right:
                left += 1
            arr[right] = arr[left]
            while arr[right] <= target and left < right:
                right -= 1
            arr[left] = arr[right]
        arr[left] = target
        self.quiksort(arr, 0, left - 1)
        self.quiksort(arr, left + 1, r)
    """
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return nums
        # self.quiksort(nums, 0, len(nums) - 1)
        nums.sort(reverse=True)
        maxarr, minarr = nums[:len(nums)//2], nums[len(nums)//2:]
        nums[0:len(nums):2] = minarr
        nums[1:len(nums):2] = maxarr

# leetcode submit region end(Prohibit modification and deletion)
