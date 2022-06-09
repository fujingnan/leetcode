# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。 
# 
#  示例 1: 
# 
#  输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s = "rat", t = "car"
# 输出: false 
# 
#  说明: 
# 你可以假设字符串只包含小写字母。 
# 
#  进阶: 
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
#  Related Topics 基础排序 哈希表
#  👍 320 👎 0

# leetcode submit region begin(Prohibit modification and deletion)
"""
直接将两个字符串排序，比较排序后是否相等。

T: O(N*logN)
S: O(1)
"""
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if not len(s) == len(t): return False
#         return sorted(s) == sorted(t)
"""
构建26个字母表，索引代表字母，元素存储字母出现频数，遍历s，将出现的字母的次数加在
对应字母表中对应的位置；再遍历t，字母每出现一次就在对应字母表的位置减1，最后判断字
母表是否全为0

T: O(N)
S: O(1)
"""
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if not len(s) == len(t): return False
#         cs = [0] * 26
#         for i in s:
#             cs[ord(i)-ord('a')] += 1
#         for j in t:
#             cs[ord(j)-ord('a')] -= 1
#         return not [k for k in cs if k]

"""
思路同上，用哈希表记录s中每个字符及其出现的次数；遍历t，将其在s的哈希表中出现的字母
对应的次数减1，最后判断哈希表中的value值是否都为0；

T: O(N)
S: O(1)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t): return False
        from collections import Counter
        cs = Counter(s)
        for i in t:
            if i in cs:
                cs[i] -= 1
        return not [k for k in cs.values() if k]
# leetcode submit region end(Prohibit modification and deletion)
