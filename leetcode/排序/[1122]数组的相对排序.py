# 给你两个数组，arr1 和 arr2， 
# 
#  
#  arr2 中的元素各不相同 
#  arr2 中的每个元素都出现在 arr1 中
#  
# 
#  对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末
# 尾。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr1.length, arr2.length <= 1000
#  0 <= arr1[i], arr2[i] <= 1000 
#  arr2 中的元素 arr2[i] 各不相同 
#  arr2 中的每个元素 arr2[i] 都出现在 arr1 中 
#  
#  Related Topics 基础排序 数组
#  👍 148 👎 0
# TODO
"""
T: O(N*logN)
S: O(N)
"""
# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         from collections import Counter
#         num_count = Counter(arr1)
#         ret, res = [], []
#         for i in arr2:
#             ret.extend([i] * num_count[i])
#             num_count -= Counter(ret)
#         for i in list(num_count.keys()):
#             res.extend([i] * num_count[i])
#         ret.extend(sorted(res))
#         return ret
"""
桶排序一：
T: O(N)
S: O(1)
"""
# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         buket = [0] * 1001
#         ret = []
#         for i in arr1:
#             buket[i] += 1
#         for j in arr2:
#             ret.extend([j] * buket[j])
#             buket[j] = 0
#         for res in range(len(buket)):
#             if res:
#                 ret.extend([res] * buket[res])
#         return ret
"""
桶排序二（simple）：
T: O(N*logN)
s: O(N)
"""
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        buket = {i: id for id, i in enumerate(arr2)}
        return sorted(arr1, key=lambda a: buket.get(a, 1000 + a))
# leetcode submit region end(Prohibit modification and deletion)
