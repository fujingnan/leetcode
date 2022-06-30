"""
https://leetcode.cn/problems/longest-common-prefix/
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        res = strs[0]
        temp = ''
        for s in strs[1:]:
            temp = ''
            for i in range(min(len(res), len(s))):
                if not res[0] == s[0]:
                    return ''
                if res[i] == s[i]:
                    temp += res[i]
                else:
                    res = temp
                    break
            res = temp
        return res