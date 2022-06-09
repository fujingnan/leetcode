from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        return self.mergeSort(nums)

    # 归并排序
    def mergeSort(self, arr):
        if len(arr) == 1:
            return arr

        def merge(arr, left, mid, right):
            p1, p2 = left, mid + 1
            helper = []
            # TODO 边界条件包括"="
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
            # TODO 先sort再merge
            sort(arr, left, mid)
            sort(arr, mid + 1, right)
            merge(arr, left, mid, right)
            return arr

        return sort(arr, 0, len(arr) - 1)

if __name__ == '__main__':
    solution = Solution()
    print(solution.sortArray([4,5,2,3,1]))