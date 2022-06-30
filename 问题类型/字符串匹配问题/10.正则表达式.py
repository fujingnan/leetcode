"""
https://leetcode.cn/problems/regular-expression-matching/
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == s:
            return True
        ns, np = len(s) + 1, len(p) + 1
        dp = [[False]*ns for _ in range(np)]
        dp[0][0] = True
        for r in range(1, np):
            if p[r-1] == '*':
                dp[r][0] = dp[r-2][0]

        for c in range(1, ns):
            for r in range(1, np):
                if s[c-1] == p[r-1] or p[r-1] == '.':
                    dp[r][c] = dp[r-1][c-1]
                elif p[r-1] == '*':
                    if p[r-2] == s[c-1] or p[r-2] == '.':
                        dp[r][c] = dp[r-2][c] or dp[r][c-1]
                    else:
                        dp[r][c] = dp[r-2][c]
        return dp[-1][-1]