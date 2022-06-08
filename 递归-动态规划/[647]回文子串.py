# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。 
# 
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。 
# 
#  
# 
#  示例 1： 
# 
#  输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#  
# 
#  示例 2： 
# 
#  输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa" 
# 
#  
# 
#  提示： 
# 
#  
#  输入的字符串长度不会超过 1000 。 
#  
#  Related Topics 字符串 动态规划 
#  👍 519 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
动态规划：
T：O（N*N）
S：O（N*N）
"""
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         row = col = len(s)
#         res = 0
#         dp = [[False] * col for _ in range(row)]
#         for i in range(row):
#             for j in range(i+1):
#                 if i == j or (i - j == 1 and s[i] == s[j]):
#                     dp[i][j], res = True, res + 1
#                 if i - j > 1 and s[i] == s[j] and dp[i-1][j+1]:
#                     dp[i][j], res = True, res + 1
#         return res
"""
中心拓展：
T：O（N*N）
S：O（N）
"""
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         str = '#' + s[0]
#         for i in s[1:]:
#             str = str + '#' + i
#         str += '#'
#         n, res = len(str), 0
#         for i in range(n):
#             res += 1
#             left, right = i - 1, i + 1
#             while left >= 0 and right < n and str[left] == str[right]:
#                 res += 1
#                 left, right = left - 1, right + 1
#         return (res-(len(s)+1)) // 2
"""
Manacher：
T：O（N）
S：O（N）
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        str = '#' + s[0]
        for i in s[1:]:
            str = str + '#' + i
        str += '#'
        n = len(str)
        res, center, rmax, dp = 0, 0, -1, [0] * n
        for i in range(n):
            if i <= rmax:
                dp[i] = min(rmax-i+1, dp[2*center-i])
            else:
                dp[i] = 1
            r, l = i+dp[i], i-dp[i]
            while (l>=0 and r<n) and str[l] == str[r]:
                dp[i] += 1
                r, l = r+1, l-1
            if r-1 > rmax and r < n:
                rmax = r - 1
                center = i
            res += dp[i] // 2
        return res

# leetcode submit region end(Prohibit modification and deletion)
