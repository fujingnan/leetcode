# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。 
# 
#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。 
# 
#  你可以假设除了整数 0 之外，这个整数不会以零开头。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
#  
# 
#  示例 2： 
# 
#  
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
#  
# 
#  示例 3： 
# 
#  
# 输入：digits = [0]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= digits.length <= 100 
#  0 <= digits[i] <= 9 
#  
#  Related Topics 数组 
#  👍 640 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
python语法
T: O(N)
S: O(1)
"""
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         digits = [str(i) for i in digits]
#         nums = int("".join(digits))
#         nums += 1
#         return [int(i) for i in str(nums)]
"""
进制法
"""
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         i = len(digits) - 1
#         while i >= 0:
#             digits[i] += 1
#             digits[i] %= 10
#             if digits[i]:
#                 return digits
#             i -= 1
#         if not digits[0]:
#             digits.insert(0, 1)
#         return digits
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = 0
        for i in range(len(digits)):
            nums += digits[i] * pow(10, len(digits)-1-i)
        return [int(i) for i in str(nums+1)]
# leetcode submit region end(Prohibit modification and deletion)
