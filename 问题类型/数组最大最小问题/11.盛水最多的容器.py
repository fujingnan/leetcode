"""
https://leetcode.cn/problems/container-with-most-water/
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height)
        left, right = 0, len(height)-1
        maxs = 0
        while left < right:
            maxs = max(maxs, (right - left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
                continue
            if height[left] > height[right]:
                right -= 1
                continue
            else:
                left += 1
                right -= 1
        return maxs