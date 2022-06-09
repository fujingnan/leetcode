# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ： 
# 
#  
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#  
# 
#  要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"111" 可以将 "1" 中的每个 "1" 映射为 "A
# " ，从而得到 "AAA" ，或者可以将 "11" 和 "1"（分别为 "K" 和 "A" ）映射为 "KA" 。注意，"06" 不能映射为 "F" ，因为 "
# 6" 和 "06" 不同。 
# 
#  给你一个只含数字的 非空 字符串 num ，请计算并返回 解码 方法的 总数 。 
# 
#  题目数据保证答案肯定是一个 32 位 的整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "0"
# 输出：0
# 解释：没有字符映射到以 0 开头的数字。含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。由于没有字符，因此没有有效的方法对此进行
# 解码，因为所有数字都需要映射。
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "06"
# 输出：0
# 解释："06" 不能映射到 "F" ，因为字符串开头的 0 无法指向一个有效的字符。 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 100 
#  s 只包含数字，并且可能包含前导零。 
#  
#  Related Topics 字符串 动态规划 
#  👍 640 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
一维数组：
如果当前数不为0且能与前一数合法结合，则当前方法数为前一方法数与前前方法数之和
"""
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if not int(s[0]) or not s:
#             return 0
#         n = len(s)
#         dp  = [1] + [0] * (n-1)
#         for i in range(1, n):
#             if int(s[i]):
#                 dp[i] = dp[i-1]
#             cur_s = 10 * (ord(s[i-1]) - ord('0')) + (ord(s[i]) - ord('0'))
#             if 10 <= cur_s <= 26:
#                 if i == 1:
#                     dp[i] += 1
#                 else:
#                     dp[i] += dp[i-2]
#         return dp[n-1]
"""
双指针
"""
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if not int(s[0]) or not s:
#             return 0
#         n, pre, cur = len(s), 1, 1
#         for i in range(1, n):
#             if int(s[i]):
#                 if s[i-1] == '1' or (s[i-1] == '2' and 0 < int(s[i]) <= 6):
#                     pre, cur = cur, cur + pre
#                 else:
#                     """
#                     如果当前数不为0但也无法与前面的数结合，那么当前方法数与前一方法数相同，即方法无新增，
#                     此时pre继续后移，即pre等于前一方法数
#                     """
#                     pre = cur
#             else:
#                 if s[i - 1] == '1' or s[i - 1] == '2':
#                     """
#                     如果当前数为0，但能与前一数结合，则当前方法数与前一方法数（当前方法数与前一方法数相同，
#                     而前一方法数又与再前方法数相同）相同，即方法数无新增
#                     """
#                     cur = pre
#                 else:
#                     """
#                     在当前数为0的情况下，只要前一数与当前数无法结合，则0必须单独计算，又由于0没有编码，则该情况无解
#                     """
#                     return 0
#         return cur

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if not int(s[0]) or not s:
#             return 0
#         dp = [1] + [0] * len(s)
#         dp[1] = 0 if s[0] == '0' else 1
#         for i in range(2, len(s)+1):
#             if 0 < int(s[i-1:i]) <= 9:
#                 dp[i] += dp[i-1]
#             if 10 <= int(s[i-2:i]) <= 26:
#                 dp[i] += dp[i-2]
#         return dp[len(s)]

"""
（1）如果当前字符不为0：

    i：不能与前一字符合法结合。因为当前字符不为0，那么当前字符也能单独成为一种解码方法，而单独解码时，方法数并无新增，仍然
    等于当前字符串之前的解码方法数；比如，"12"解码数为2，如果不考虑"22"结合，"122"的解码方法数也为2；
    
    ii：能与前一字符结合。考虑不结合的情况，即为i。考虑结合的情况，当前字符与前一字符结合看成一个字符，那么情况就和前前种
    情况一样，所以整体解码方法数等于情况i加上前前种方法数
    
（2）如果当前字符为0：
    i：能与前一字符结合。由于0不能单独解码，因此能与前一字符结合就与前一字符结合后看成一个字符，那么情况就和前前种情况一样，
    整体解码方法数等于前前种情况下的方法数
    ii：不能与前一字符结合。由于0既不能单独解码，又无法与前一字符结合编码，因此这种情况无解。
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        pre_pre, cur, pre_s = 0, s[0] > '', ''
        for _s in s:
            pre_pre, cur, pre_s = cur, (_s > '0') * cur + ('10' <= pre_s + _s <= '26') * pre_pre, _s
        return cur
# leetcode submit region end(Prohibit modification and deletion)
