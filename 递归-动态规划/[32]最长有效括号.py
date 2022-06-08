# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = ""
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 3 * 104 
#  s[i] 为 '(' 或 ')' 
#  
#  
#  
#  Related Topics 字符串 动态规划 
#  👍 1228 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
栈：
T：O（N）
S：O（N）
"""
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         stack = [-1]
#         maxvalid = 0
#         for i in range(len(s)):
#             if s[i] == '(':
#                 stack.append(i)
#             else:
#                 stack.pop()
#             if not stack:
#                 stack.append(i)
#             print(stack, i)
#             maxvalid = max(maxvalid, i - stack[-1])
#         return maxvalid

"""
双指针：
T: O(N)
S: O(1)
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = maxvalid = 0
        for i in s:
            if i == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxvalid = max(maxvalid, right*2)
            elif left < right:
                left = right = 0
        j = len(s) - 1
        left = right = 0
        while j >= 0:
            if s[j] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxvalid = max(maxvalid, right*2)
            elif left > right:
                left = right = 0
            j -= 1
        return maxvalid
"""
动态规划-完整版（按照原理细节逐行编写，简单易懂）：
T：O（N）
S：O（N）
"""
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         n = len(s)
#         dp = [0] * n
#         maxvalid = 0
#         for i in range(n):
#             if i - 1 >= 0:
#                 if s[i] == '(':
#                     dp[i] = 0
#                 elif s[i - 1] == '(':
#                     if i - 2 >= 0:
#                         dp[i] = dp[i-2] + 2
#                     else:
#                         dp[i] += 2
#                 else:
#                     if i - dp[i - 1] - 1 < 0 or s[i - dp[i - 1] - 1] == ')':
#                         dp[i] = 0
#                     else:
#                         if i - dp[i - 1] - 2 >= 0:
#                             dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
#                         else:
#                             dp[i] = dp[i - 1] + 2
#             maxvalid = max(maxvalid, dp[i])
#         return maxvalid
"""
动态规划-简洁版
"""
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         n = len(s)
#         dp = [0] * n
#         maxvalid = 0
#         for i in range(n):
#             if i - 1 >= 0 and s[i] == ')':
#                 if s[i - 1] == '(':
#                     dp[i] = dp[i - 2] + 2
#                 elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
#                     dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
#             maxvalid = max(maxvalid, dp[i])
#         return maxvalid
# leetcode submit region end(Prohibit modification and deletion)
