"""
https://leetcode.cn/problems/3sum/
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        res = []
        nums.sort()
        for p1 in range(0, len(nums)-2):
            if p1 and nums[p1] == nums[p1 - 1]:
                continue
            left = p1 + 1
            right = len(nums)-1
            while left < right:
                if left > p1+1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                if right < len(nums)-1 and nums[right] == nums[right+1]:
                    right -= 1
                    continue
                if nums[p1]+nums[left]+nums[right]==0:
                    res.append([nums[p1], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[p1]+nums[left]+nums[right]<0:
                    left += 1
                else:
                    right -= 1
        return res