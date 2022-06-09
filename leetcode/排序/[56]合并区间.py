# 给出一个区间的集合，请合并所有重叠的区间。 
# 
#  
# 
#  示例 1: 
# 
#  输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2: 
# 
#  输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。 
# 
#  注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。 
# 
#  
# 
#  提示： 
# 
#  
#  intervals[i][0] <= intervals[i][1]
#  
#  Related Topics 基础排序 数组
#  👍 755 👎 0

"""
1. 先按照每个区间的下限排序，从小到大，保证区间的相对连续性。
2. 遍历区间数组，用一个变量 maxn 记录当前区间与下一区间的上限的最大值，maxn初始化
   为第一个区间的上限，如果 maxn 大于等于下一个区间的下限，两区间必然重叠；
3. 若 maxn 不再大于等于下一个区间的下限，则记录该次遍历最小值与 maxn 为合并后区间

T: O(N*logN)
S: O(N)
"""

# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         if not intervals: return []
#         if len(intervals) == 1: return intervals
#         intervals.sort(key=lambda x: x[0])
#         res, i, size = [], 0, len(intervals) - 1
#         while i <= size:
#             j = i
#             maxn = intervals[j][1]
#             while i + 1 <= size and maxn >= intervals[i + 1][0]:
#                 maxn = max(maxn, intervals[i + 1][1])
#                 i += 1
#             res.append([intervals[j][0], maxn])
#             i += 1
#         return res
"""
简洁版
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        if len(intervals) == 1: return intervals
        res = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if res and i[0] <= res[-1][1]:
                res[-1][1] = max(i[1], res[-1][1])
            else:
                res.append(i)
        return res

# leetcode submit region end(Prohibit modification and deletion)
