# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。 
#  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。 
#  你可以按任意顺序返回答案。 
#  
#  Related Topics 堆 哈希表 
#  👍 636 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
桶排序
T: O(N)
S: O(N)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        nums2count = Counter(nums)
        offset = max([v for _, v in nums2count.items()])
        buket = [[] for _ in range(offset+1)]
        for n, v in nums2count.items():
            buket[v].append(n)
        b_sorts = [j for i in buket for j in i]
        return b_sorts[::-1][:k]
'''
利用小根堆
T: O(N*logK)
S: O(N)+O(K)
'''
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         import heapq
#         from collections import Counter
#         nums2count = Counter(nums)
#         quque = []
#         heapq.heapify(quque)
#         for n, c in nums2count.items():
#             if not len(quque) == k:
#                 heapq.heappush(quque, (c, n))
#             else:
#                 if quque[0][0] < c:
#                     # heapq.heappop(hq)
#                     # heapq.heappush(hq, (c, n))
#                     heapq.heapreplace(quque, (c, n))
#         res = []
#         for i in quque:
#             res.append(i[1])
#         return res
"""
直接排序
"""
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         from collections import Counter
#         nums_cn = Counter(nums)
#         sorts = sorted(dict(nums_cn).items(), key=lambda x: x[1], reverse=True)
#         print(sorts)
#         return [i for i, _ in sorts[:k]]
# leetcode submit region end(Prohibit modification and deletion)
