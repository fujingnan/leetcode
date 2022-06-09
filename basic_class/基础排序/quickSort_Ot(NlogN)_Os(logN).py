# encoding=utf-8
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        return self.quickSort(nums)

    # 快速排序
    def quickSort(self, nums):
        if len(nums) == 1:
            return nums

        def partition(arr, left, right):
            mid = left + ((right - left) >> 1)
            target = arr[mid]
            arr[mid], arr[right] = arr[right], arr[mid]
            while left < right:
                while left < right and arr[left] <= target:
                    left += 1
                arr[right] = arr[left]
                while left < right and arr[right] >= target:
                    right -= 1
                arr[left] = arr[right]
            arr[left] = target
            return left

        def sort(arr, left, right):
            if left >= right:
                return
            pivot = partition(arr, left, right)
            # TODO 易错写成sort(arr, left, pivot)
            sort(arr, left, pivot - 1)
            sort(arr, pivot + 1, right)
            return arr

        return sort(nums, 0, len(nums) - 1)

if __name__ == '__main__':
    solution = Solution()
    res = solution.sortArray([5,3,2,3,1])
    print(res)