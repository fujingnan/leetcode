# 给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。 
# 
#  返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组。
#  
# 
#  示例: 
# 
#  输入: array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]
# 输出: [1, 3]
#  
# 
#  示例:
# 
#  输入: array1 = [1, 2, 3], array2 = [4, 5, 6]
# 输出: [] 
# 
#  提示： 
# 
#  
#  1 <= array1.length, array2.length <= 100000 
#  
#  Related Topics 基础排序 数组
#  👍 16 👎 0
"""
先求出两数组和的差值，两数组加起来处除2的值即为交换后两数组各自的和，由于不管如何交换值，
两数组加起来的总和是不变的，所以若两数组和之差为奇数，则无法找到能够使得两数组之和能够均
分的交换值
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        if not array2: return []
        if len(array1) == 1 and len(array2) == 1 and not array1 == array2: return []
        diff = abs(sum(array1) - sum(array2))
        if diff % 2: return []
        for x in set(array1):
            if x+diff//2 in set(array2):
                return [x, x+diff//2]
        for y in set(array2):
            if y + diff // 2 in set(array1):
                return [y + diff // 2, y]
        return []
# leetcode submit region end(Prohibit modification and deletion)
