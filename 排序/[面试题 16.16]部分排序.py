# 给定一个整数数组，编写一个函数，找出索引m和n，只要将索引区间[m,n]的元素排好序，整个数组就是有序的。注意：n-m尽量最小，也就是说，找出符合条件的最短
# 序列。函数返回值为[m,n]，若不存在这样的m和n（例如整个数组是有序的），请返回[-1,-1]。 
#  示例： 
#  输入： [1,2,4,7,10,11,7,12,6,7,16,18,19]
# 输出： [3,9]
#  
#  提示： 
#  
#  0 <= len(array) <= 1000000
#  
#  Related Topics 排序 数组
#  👍 55 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
T: O(N)
S: O(1)
"""
# class Solution:
#     def subSort(self, array: List[int]) -> List[int]:
#         if not array or len(array) == 1: return [-1, -1]
#         m = n = -1
#         maxn, minn = -float("inf"), float("inf")
#         for i in range(len(array)):
#             if array[i] >= maxn:
#                 maxn = array[i]
#             else:
#                 n = i
#         j = len(array) - 1
#         while j >= 0:
#             if array[j] <= minn:
#                 minn = array[j]
#             else:
#                 m = j
#             j -= 1
#         return [m, n]

"""
T: O(N*logN)
s: O(1)
"""
class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        if not array:
            return [-1, -1]
        sa = sorted(array)
        i, j = 0, len(array) - 1
        while i < len(array) and array[i] == sa[i]:
            i += 1
        while j >= 0 and array[j] == sa[j]:
            j -= 1
            if i >= j:
                return [-1, -1]
        return [i, j]
# leetcode submit region end(Prohibit modification and deletion)
