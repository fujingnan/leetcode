# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
#  
# 
#  示例 2： 
# 
#  输入：arr = [0,1,2,1], k = 1
# 输出：[0] 
# 
#  
# 
#  限制： 
# 
#  
#  0 <= k <= arr.length <= 10000 
#  0 <= arr[i] <= 10000 
#  
#  Related Topics 堆 分治算法 
#  👍 182 👎 0

"""
直接法：排序后取前k个数

T: O(N*logN)
S: O(1)
"""
# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         if not arr or not k:
#             return []
#         arr = sorted(arr)
#         return arr[0:k]
"""
bfprt
"""
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or not k:
            return []
        self.bfprt(arr, 0, len(arr)-1, k-1)
        return arr[:k]

    def bfprt(self, arr, left, right, k):
        if left == right:
            return arr[left]
        pivot = self.midOfmid(arr, left, right)
        pivot_range = self.partition(arr, left, right, pivot)
        if k >= pivot_range[0] and k <= pivot_range[1]:
            return arr[k]
        elif k < pivot_range[0]:
            return self.bfprt(arr, left, pivot_range[0]-1, k)
        else:
            return self.bfprt(arr, pivot_range[1]+1, right, k)

    def midOfmid(self, arr, left, right):
        arrSize = right - left + 1
        offset = 1 if arrSize % 5 else 0
        midArrSize = arrSize // 5 + offset
        midArr, i = [], 0
        while i < midArrSize:
            start = left + i * 5
            end = start + 4
            midArr.append(self.getMid(arr, start, min(end, right)))
            i += 1
        return self.bfprt(midArr, 0, len(midArr)-1, len(midArr)//2)

    def getMid(self, arr, left, right):
        self.insertionSort(arr, left, right)
        mid = left + ((right - left) >> 2)
        return arr[mid]

    def insertionSort(self, arr, left, right):
        for i in range(left+1, right+1):
            while i > left:
                if arr[i] < arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                    i -= 1
                else:
                    break
    def partition(self, arr, left, right, pivot):
        small = left - 1
        cur = left
        big = right + 1
        while not cur == big:
            if arr[cur] < pivot:
                small += 1
                arr[cur], arr[small] = arr[small], arr[cur]
                cur += 1
            elif arr[cur] > pivot:
                big -= 1
                arr[cur], arr[big] = arr[big], arr[cur]
            else:
                cur += 1
        return [small+1, big-1]

# leetcode submit region end(Prohibit modification and deletion)
