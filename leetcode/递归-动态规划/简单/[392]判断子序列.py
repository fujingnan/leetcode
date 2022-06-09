# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。 
# 
#  你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。 
# 
#  字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"ae
# c"不是）。 
# 
#  示例 1: 
# s = "abc", t = "ahbgdc" 
# 
#  返回 true. 
# 
#  示例 2: 
# s = "axc", t = "ahbgdc" 
# 
#  返回 false. 
# 
#  后续挑战 : 
# 
#  如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码
# ？ 
# 
#  致谢: 
# 
#  特别感谢 @pbrother 添加此问题并且创建所有测试用例。 
#  Related Topics 贪心算法 二分查找 动态规划 
#  👍 360 👎 0
"""
利用队列和栈的思路：
1. 将s和t拼接，s在t前
2. 利用快慢指针。让快指针先走到t的开头位置，慢指针初始化在s开头，
   然后判断两个指针所指字符是否相等，若相等，n+1，并且两指正同时右移；
3. 若end指针到头或者start指针到头，结束遍历，若n和s长度相等，返回true；
   否则，返回false
T: O(N)
S: O(1)
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
        n, m = len(s), len(t)
        i = j = 0
        while i<n and j<m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n
# leetcode submit region end(Prohibit modification and deletion)
