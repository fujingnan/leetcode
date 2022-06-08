# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。 
# 
#  你需要返回给定数组中的重要翻转对的数量。 
# 
#  示例 1: 
# 
#  
# 输入: [1,3,2,3,1]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  
# 输入: [2,4,3,5,1]
# 输出: 3
#  
# 
#  注意: 
# 
#  
#  给定数组的长度不会超过50000。 
#  输入数组中的所有数字都在32位整数的表示范围内。 
#  
#  Related Topics 排序 树状数组 线段树 二分查找 分治算法 
#  👍 251 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
利用归并排序，在归并的过程中产生逆序对问题。这里需要注意的是，计算逆序对的数量
必须发生在每次归并排序前，也就是在每轮 merge 之前，就需要把当前 mid 的前后部
分拿来统计一遍逆序对数量，这样能保证每次计算时，计算的是原数组里元素大小的相对
顺序。

T: O(N*logN)
S: O(N)
"""
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, arr, l, r):
        if l == r: return 0
        mid = l + ((r - l) >> 1)
        return self.mergeSort(arr, l, mid) \
               + self.mergeSort(arr, mid + 1, r) \
               + self.merge(arr, l, mid, r)

    def merge(self, arr, l, mid, r):
        res = []
        p1, p2, count = l, mid + 1, 0
        i = p1
        for j in arr[p2:r+1]:
            while i <= mid and arr[i] <= 2*j:
                i += 1
            count += mid - i + 1
        while p1 <= mid and p2 <= r:
            if arr[p1] <= arr[p2]:
                res.append(arr[p1])
                p1 += 1
            else:
                res.append(arr[p2])
                p2 += 1
        while p1 <= mid:
            res.append(arr[p1])
            p1 += 1
        while p2 <= r:
            res.append(arr[p2])
            p2 += 1
        for i in range(len(res)):
            arr[l + i] = res[i]
        return count

# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         if len(nums) < 2: return 0
#         return self.mergeSort(nums, 0, len(nums) - 1)
#     def mergeSort(self, arr, l, r):
#         if l >= r: return 0
#         mid = l + ((r - l) >> 1)
#         count = self.mergeSort(arr, l, mid) \
#                 + self.mergeSort(arr, mid + 1, r)
#         help = []
#         p1, p2 = l, mid + 1
#         p = p1
#         while p2 <= r:
#             while p <= mid and arr[p] <= 2*arr[p2]:
#                 p += 1
#             while p1 <= mid and arr[p1] < arr[p2]:
#                 help.append(arr[p1])
#                 p1 += 1
#             help.append(arr[p2])
#             count += mid - p + 1
#             p2 += 1
#         while p1 <= mid:
#             help.append(arr[p1])
#             p1 += 1
#         for i in range(len(help)):
#             arr[l + i] = help[i]
#         return count

# leetcode submit region end(Prohibit modification and deletion)
