# 给定一个整数数组，找出总和最大的连续数列，并返回总和。 
# 
#  示例： 
# 
#  输入： [-2,1,-3,4,-1,2,1,-5,4]
# 输出： 6
# 解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
#  
# 
#  进阶： 
# 
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
#  Related Topics 数组 分治算法 动态规划 
#  👍 56 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return None
        size = len(nums)
        if size == 1: return nums[0]
        sum, maxn = 0, -float("inf")
        for i in range(size):
            sum += nums[i]
            maxn = max(sum, maxn)
            if sum < 0: sum = 0
        return maxn
# leetcode submit region end(Prohibit modification and deletion)
