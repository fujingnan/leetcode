"""
https://leetcode.cn/problems/longest-palindromic-substring/
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        dp = [[False]*len(s) for _ in range(len(s))]
        maxl = 0
        start = end = 0
        for right in range(1, len(s)):
            for left in range(0, right):
                if s[left] == s[right] and (right-left<=2 or dp[left+1][right-1]):
                    dp[left][right] = True
                    if right - left + 1 > maxl:
                        maxl = right - left + 1
                        start = left
                        end = right
        return s[start:end+1]