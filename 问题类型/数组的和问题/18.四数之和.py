"""
https://leetcode.cn/problems/4sum/
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        size = len(nums)
        res = []
        for p1 in range(0, size - 3):
            if p1 and nums[p1] == nums[p1 - 1]:
                continue
            if nums[p1] * 4 > target:
                break
            # p2的起始点错写成p1
            for p2 in range(p1 + 1, size - 2):
                # p2 > p1 + 1 错写成p2
                if p2 > p1 + 1 and nums[p2] == nums[p2 - 1]:
                    continue
                if nums[p2] * 3 > target - nums[p1]:
                    break
                left = p2 + 1
                right = size - 1
                while left < right:
                    if left > p2 + 1 and nums[left] == nums[left - 1]:
                        # 漏掉
                        left += 1
                        continue
                    if right < size - 1 and nums[right] == nums[right + 1]:
                        # 漏掉
                        right -= 1
                        continue
                    if nums[left] * 2 > target - nums[p1] - nums[p2]:
                        break
                    if nums[p1] + nums[p2] + nums[left] + nums[right] == target:
                        res.append([nums[p1], nums[p2], nums[left], nums[right]])
                        # 漏掉
                        left += 1
                        right -= 1
                    elif nums[p1] + nums[p2] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
        return res
