from typing import List


class Solution:

    def __init__(self, opt):
        self.opt = opt

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        if self.opt == 'choice':
            return self.choiceSort(nums)
        if self.opt == 'bubble':
            return self.bubbleSort(nums)
        if self.opt == 'insert':
            return self.insertSort(nums)
        if self.opt == 'quick':
            return self.quickSort(nums)
        if self.opt == 'merge':
            return self.mergeSort(nums)
        if self.opt == 'heap':
            return self.heapSort(nums)

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
            sort(arr, left, pivot - 1)
            sort(arr, pivot + 1, right)
            return arr

        return sort(nums, 0, len(nums) - 1)

    # 归并排序
    def mergeSort(self, arr):
        if len(arr) == 1:
            return arr

        def merge(arr, left, mid, right):
            p1, p2 = left, mid + 1
            helper = []
            while p1 <= mid and p2 <= right:
                if arr[p1] < arr[p2]:
                    helper.append(arr[p1])
                    p1 += 1
                else:
                    helper.append(arr[p2])
                    p2 += 1
            while p1 <= mid:
                helper.append(arr[p1])
                p1 += 1
            while p2 <= right:
                helper.append(arr[p2])
                p2 += 1
            for i in range(len(helper)):
                arr[left + i] = helper[i]
            return arr

        def sort(arr, left, right):
            if left == right:
                return
            mid = left + ((right - left) >> 1)
            sort(arr, left, mid)
            sort(arr, mid + 1, right)
            merge(arr, left, mid, right)
            return arr

        return sort(arr, 0, len(arr) - 1)

    # 堆排序
    def heapSort(self, nums):
        if len(nums) == 1:
            return nums

        def heapInsert(arr, index):
            """
            自底向上，根据数组一次性构建大根堆
            """
            father = (index - 1) // 2
            while index > 0 and arr[index] > arr[father]:
                arr[index], arr[father] = arr[father], arr[index]
                index = father
                father = (index - 1) // 2

        def heapipy(arr, index, size):
            """
            自顶向下，不断将当前数组重新调整为大根堆
            """
            left = index * 2 + 1
            right = left + 1
            largestIndex = 0
            # 错点: index < size
            while left < size:
                # 卡点
                if right < size and arr[left] < arr[right]:
                    largestIndex = right
                else:
                    largestIndex = left
                largestIndex = largestIndex if arr[largestIndex] > arr[index] else index
                if largestIndex == index:
                    break
                arr[index], arr[largestIndex] = arr[largestIndex], arr[index]
                index = largestIndex
                left = index * 2 + 1
                right = left + 1

        def sort(arr):
            """
            根据heapInsert和heapify排序数组
            """
            for i in range(len(arr)):
                heapInsert(arr, i)
            size = len(arr)
            arr[0], arr[size - 1] = arr[size - 1], arr[0]
            size -= 1
            while size > 0:
                heapipy(arr, 0, size)
                arr[0], arr[size - 1] = arr[size - 1], arr[0]
                size -= 1
            return arr

        return sort(nums)


if __name__ == '__main__':
    solution = Solution('heap')
    res = solution.sortArray([5, 2, 3, 1, 1, 6, 0, 4])
    print(res)
