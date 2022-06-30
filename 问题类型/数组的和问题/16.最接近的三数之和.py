"""
https://leetcode.cn/problems/3sum-closest/
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        size = len(nums)
        nums.sort()
        diff = float('inf')
        res = 0
        for p in range(size-2):
            if p and nums[p] == nums[p-1]:
                continue
            left, right = p+1, size-1
            while left < right:
                cur = nums[left] + nums[right] + nums[p]
                if cur == target:
                    return target
                if abs(cur - target) < diff:
                    diff = abs(cur - target)
                    res = cur
                if cur < target:
                    left += 1
                else:
                    right -= 1
        return res