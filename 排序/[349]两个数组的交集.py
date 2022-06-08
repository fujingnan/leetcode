# 给定两个数组，编写一个函数来计算它们的交集。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
#  
# 
#  示例 2： 
# 
#  输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4] 
# 
#  
# 
#  说明： 
# 
#  
#  输出结果中的每个元素一定是唯一的。 
#  我们可以不考虑输出结果的顺序。 
#  
#  Related Topics 排序 哈希表 双指针 二分查找
#  👍 301 👎 0

"""
暴力法/直接法
T: O(max(nums1.len, nums2.len))
S: O(max(nums1.len, nums2.len))
"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2: return []
        if len(nums1) == 1: return nums1
        if len(nums2) == 1: return nums2
        nums2 = {nums2[i]: i for i in range(len(nums2))}
        ret = set()
        for i in nums1:
            if i in nums2:
                ret.add(i)
        return list(ret)
# leetcode submit region end(Prohibit modification and deletion)
