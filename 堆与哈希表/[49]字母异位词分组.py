# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。 
# 
#  示例: 
# 
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ] 
# 
#  说明： 
# 
#  
#  所有输入均为小写字母。 
#  不考虑答案输出的顺序。 
#  
#  Related Topics 哈希表 字符串 
#  👍 654 👎 0

"""
利用哈希表：
--key: 每个字符串中按字母顺序排序后组成的新字符串
--value: 每个key对应的原顺序字符串的集合
T: O(N*K*logK)
S: O(N*K)
"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}
        for s in strs:
            res_dict.setdefault("".join(sorted(list(s))), []).append(s)
        return list(res_dict.values())
"""
利用桶计数
T: O(N*K)
S: O(N*K)
"""
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res_dict = {}
#         for s in strs:
#             char_l = [0] * 26
#             for w in s:
#                 char_l[ord(w) - ord('a')] += 1
#             res_dict.setdefault(str(char_l), []).append(s)
#         return list(res_dict.values())
# leetcode submit region end(Prohibit modification and deletion)
