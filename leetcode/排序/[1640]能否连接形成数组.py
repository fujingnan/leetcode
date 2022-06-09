# 给你一个整数数组 arr ，数组中的每个整数 互不相同 。另有一个由整数数组构成的数组 pieces，其中的整数也 互不相同 。请你以 任意顺序 连接 pi
# eces 中的数组以形成 arr 。但是，不允许 对每个数组 pieces[i] 中的整数重新排序。 
# 
#  如果可以连接 pieces 中的数组形成 arr ，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [85], pieces = [[85]]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [15,88], pieces = [[88],[15]]
# 输出：true
# 解释：依次连接 [15] 和 [88]
#  
# 
#  示例 3： 
# 
#  
# 输入：arr = [49,18,16], pieces = [[16,18,49]]
# 输出：false
# 解释：即便数字相符，也不能重新排列 pieces[0]
#  
# 
#  示例 4： 
# 
#  
# 输入：arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
# 输出：true
# 解释：依次连接 [91]、[4,64] 和 [78] 
# 
#  示例 5： 
# 
#  
# 输入：arr = [1,3,5,7], pieces = [[2,4,6,8]]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= pieces.length <= arr.length <= 100 
#  sum(pieces[i].length) == arr.length 
#  1 <= pieces[i].length <= arr.length 
#  1 <= arr[i], pieces[i][j] <= 100 
#  arr 中的整数 互不相同 
#  pieces 中的整数 互不相同（也就是说，如果将 pieces 扁平化成一维数组，数组中的所有整数互不相同） 
#  
#  Related Topics 基础排序 数组
#  👍 14 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
直接法：由于pieces中的整数不允许调整顺序，因此判断peices能否拼接成与arr一样的数组，只需要判断arr中
每个元素是否与pieces中每个子数组的第一个元素相等，如果相等，再拼接后判断即可
T: O(N)
S: O(N)
"""
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        if len(pieces) == 1 and not pieces[0] == arr: return False
        if len(pieces) == 1 and pieces[0] == arr: return True
        first_n = {l[0]: l for l in pieces}
        sub = []
        for i in arr:
            if i in first_n:
                sub.extend(first_n[i])
            # 不能加以下else代码，因为arr中的元素有可能不等于pieces子数组的第一个元素！
            # else:
            #     print(i, first_n)
            #     return False
        return sub == arr
# leetcode submit region end(Prohibit modification and deletion)
