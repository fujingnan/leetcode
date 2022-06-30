"""
https://leetcode.cn/problems/valid-parentheses/
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        maps = {'(': ')', '[': ']', '{': '}'}
        # 错：stack[s[0]]
        stack = []
        for i in range(len(s)):
            if s[i] in maps:
                stack.append(s[i])
            else:
                if stack and maps[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        # 易漏
        else:
            return False
