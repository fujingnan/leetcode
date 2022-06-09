from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        return self.heapSort(nums)

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