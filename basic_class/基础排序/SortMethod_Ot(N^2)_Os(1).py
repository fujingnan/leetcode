from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        return self.insertSort(nums)

    # 选择排序
    def choiceSort(self, nums):
        if len(nums) == 1:
            return nums
        right = len(nums) - 1
        for i in range(right):
            minum = nums[i]
            minid = i
            for j in range(i + 1, right + 1):
                if nums[j] < minum:
                    minum = nums[j]
                    minid = j
            nums[i], nums[minid] = nums[minid], nums[i]
        return nums

    # 冒泡排序
    def bubbleSort(self, nums):
        if len(nums) == 1:
            return nums
        left, right = 0, len(nums) - 1
        while right >= 0:
            for i in range(right):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            right -= 1
        return nums

    # 插入排序
    def insertSort(self, nums):
        if len(nums) == 1:
            return nums
        right = len(nums)
        for i in range(1, right):
            while i > 0:
                if nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
                i -= 1
        return nums
