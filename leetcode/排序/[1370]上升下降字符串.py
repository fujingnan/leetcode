# 给你一个字符串 s ，请你根据下面的算法重新构造字符串： 
# 
#  
#  从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。 
#  从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。 
#  重复步骤 2 ，直到你没法从 s 中选择字符。 
#  从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。 
#  从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。 
#  重复步骤 5 ，直到你没法从 s 中选择字符。 
#  重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。 
#  
# 
#  在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。 
# 
#  请你返回将 s 中字符重新排序后的 结果字符串 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "aaaabbbbcccc"
# 输出："abccbaabccba"
# 解释：第一轮的步骤 1，2，3 后，结果字符串为 result = "abc"
# 第一轮的步骤 4，5，6 后，结果字符串为 result = "abccba"
# 第一轮结束，现在 s = "aabbcc" ，我们再次回到步骤 1
# 第二轮的步骤 1，2，3 后，结果字符串为 result = "abccbaabc"
# 第二轮的步骤 4，5，6 后，结果字符串为 result = "abccbaabccba"
#  
# 
#  示例 2： 
# 
#  输入：s = "rat"
# 输出："art"
# 解释：单词 "rat" 在上述算法重排序以后变成 "art"
#  
# 
#  示例 3： 
# 
#  输入：s = "leetcode"
# 输出："cdelotee"
#  
# 
#  示例 4： 
# 
#  输入：s = "ggggggg"
# 输出："ggggggg"
#  
# 
#  示例 5： 
# 
#  输入：s = "spo"
# 输出："ops"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 500 
#  s 只包含小写英文字母。 
#  
#  Related Topics 基础排序 字符串
#  👍 79 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
如果允许使用内置函数，可利用sort进行排序，利用collections的Counter方法进行计数:
1. 利用counter统计出各个字符在s中的数量
2. 取出s中出现的字符
3. 将字符先按照升序排列，并将字符串累加
4. s中各个字符出现的次数分别全部减去1
5. 回到第3步，但是按照相反的次序排列
6. 如果s中各个字符出现的次数都减到0，返回

T: O(N*logN)
S: O(N)
"""
# class Solution:
#     def sortString(self, s: str) -> str:
#         from collections import Counter as counter
#         str_count = counter(s)
#         concat, flag = '', False
#         while str_count:
#             res_str = list(str_count.keys())
#             res_str.sort(reverse=flag)
#             flag = not flag
#             concat += ''.join(res_str)
#             str_count -= counter(res_str)
#         return concat
"""
桶计数
T: O(N)
S: O(1)
"""
class Solution:
    def sortString(self, s: str) -> str:
        if len(s) == 1: return s
        buket, concat = [0] * 26, ''
        for i in s:
            buket[ord(i) - ord('a')] += 1
        while not len(concat) == len(s):
            for up in range(len(buket)):
                if buket[up] <= 0:
                    continue
                concat += chr(up + ord('a'))
                buket[up] -= 1
            for down in range(25, -1, -1):
                if buket[down] <= 0:
                    continue
                concat += chr(down + ord('a'))
                buket[down] -= 1
        return concat
"""
队列: 利用两个栈实现队列功能，先对s进行排序，压入第一个栈，再从栈中依次弹出元素压入第二个栈，
于是第二个栈取元素就会按照队列先进先出的规则输出了。循环执行从第一个栈入第二个栈，再从第二个
栈入第一个栈，每次遍历栈都按照题目要求将栈中元素弹出给结果，直到栈为空，退出循环。

T: O(N*logN)
S: O(N)
"""
# class Solution:
#     def sortString(self, s: str) -> str:
#         down = sorted(list(s))
#         ret, up = '', [down.pop() for _ in range(len(down))]
#         while not len(ret) == len(s):
#             ret += up.pop()
#             while up:
#                 if up[-1] > ret[-1]:
#                     ret += up.pop()
#                 else:
#                     down.append(up.pop())
#             if down: ret += down.pop()
#             while down:
#                 if not down: break
#                 if down[-1] < ret[-1]:
#                     ret += down.pop()
#                 else:
#                     up.append(down.pop())
#         return ret
# leetcode submit region end(Prohibit modification and deletion)
