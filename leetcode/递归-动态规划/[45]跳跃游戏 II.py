# 给定一个非负整数数组，你最初位于数组的第一个位置。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。 
# 
#  示例: 
# 
#  输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#  
# 
#  说明: 
# 
#  假设你总是可以到达数组的最后一个位置。 
#  Related Topics 贪心算法 数组 
#  👍 869 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
双指针：以[2,2,4,1,5,3,1,7]为例：
（1）从数组的第一个位置2开始，第一个位置所能跳跃到的所有位置的跳跃次数都为1，即dp=[1,1,1,0,0,0,0,0]；
（2）slow就从第二个位置2开始，fast从第一个位置能跳跃到的最远距离的下一个位置1开始走，如果第二个位置所
能跳跃的最大距离能够超过或等于fast所在的位置，那么fast从当前位置一直走到第二个位置所能跳跃到的最远距离那个位
置，为1，于是第二个位置从fast开始到其所能跳跃到的最远距离所经过的所有位置的跳跃次数都为第二个位置的跳跃
次数加上1，即dp=[1,1,1,2,0,0,0,0]，然后slow前进一步，fast跳到第二个位置所能跳跃到的最远距离的下一个位置；
如果如果第二个位置所能跳跃的最大距离达不到fast所在的位置，那么slow继续走到下一个位置，fast保持不变，由于
题目规定总能到达目的地，因此不会出现slow越过fast的情况；
（3）以此类推
总结：说白了，就是先看第一个位置能到达的所有位置是哪些，到达这些位置的跳跃次数都为1，毕竟是从第一个位置一步到达的，
而后面的每一个位置所能到达的位置都为到达每一个位置起跳点的跳跃次数加上1，对于同一个起跳点，它所能到达的任何位置的
最小跳跃次数都是一样的，而利用fast指针是为了避免计算已经计算过的位置，直接从上一个起跳点跳跃极限的下一个位置开始
算，同时slow也从新的起跳点开始算
T：O（N）
S：O（N）
"""
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 0
#         dp = [0] * len(nums)
#         for i in range(min(nums[0]+1, len(nums))):
#             dp[i] = 1
#         slow, fast = 1, nums[0] + 1
#         while fast < len(nums):
#             if fast-slow <= nums[slow]:
#                 for i in range(fast, min(slow+nums[slow]+1, len(nums))):
#                     dp[i] = dp[slow] + 1
#                 fast = min(slow + nums[slow] + 1, len(nums))
#                 slow += 1
#             else:
#                 slow += 1
#         return dp[-1]

class Solution:
    def jump(self, nums: List[int]) -> int:
        maxdist, end, res = 0, 0, 0
        for i in range(len(nums)-1):
            maxdist = max(maxdist, i + nums[i])
            if i == end:
                end = maxdist
                res += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
