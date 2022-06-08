# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#  
# 
#  示例 2： 
# 
#  
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] 仅由小写英文字母组成 
#  
#  Related Topics 字符串 
#  👍 1536 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
横向扫描：
T：O（mn）
S：O（1）
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        temp, res = '', strs[0]
        for s in strs[1:]:
            temp = ''
            for i in range(min(len(res), len(s))):
                if not s[0] == res[0]:
                    return ''
                if res[i] == s[i]:
                    temp += s[i]
                else:
                    break
            res = temp
        return res
"""
利用python特性
"""
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ''
#         res, flag = '', 0
#         for i in zip(*strs):
#             if not flag and not len(set(i)) == 1:
#                 return ''
#             flag = 1
#             if len(set(i)) == 1:
#                 res += i[0]
#             else:
#                 break
#         return res
# leetcode submit region end(Prohibit modification and deletion)
