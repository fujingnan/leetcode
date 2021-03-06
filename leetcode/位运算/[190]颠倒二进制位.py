# 颠倒给定的 32 位无符号整数的二进制位。 
# 
#  
# 
#  示例 1： 
# 
#  输入: 00000010100101000001111010011100
# 输出: 00111001011110000010100101000000
# 解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
#      因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。
# 
#  示例 2： 
# 
#  输入：11111111111111111111111111111101
# 输出：10111111111111111111111111111111
# 解释：输入的二进制串 11111111111111111111111111111101 表示无符号整数 4294967293，
#      因此返回 3221225471 其二进制表示形式为 10111111111111111111111111111111 。 
# 
#  
# 
#  提示： 
# 
#  
#  请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的
# 还是无符号的，其内部的二进制表示形式都是相同的。 
#  在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 2 中，输入表示有符号整数 -3，输出表示有符号整数 -10737418
# 25。 
#  
# 
#  
# 
#  进阶: 
# 如果多次调用这个函数，你将如何优化你的算法？ 
#  Related Topics 位运算 
#  👍 252 👎 0

# leetcode submit region begin(Prohibit modification and deletion)
"""
右移法：
1. (n >> i) & 1 ===> (n >> i) & 000...1，表示每次取得n的最高位；
2. ((n >> i) & 1) << 31 - i 表示将取得的n的最高位每次左移i位，将最高位的位置腾出来
    给新的n的最高位占位，以此类推
3. res | ((n >> i) & 1) << 31 - i 表示把第二步中每次得到的最高位的结果放到res的对
   应位置上占位，全部放完后，就得到倒序结果了
"""
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res, i = 0, 0
#         while i <= 31:
#             res |= ((n >> i) & 1) << 31 - i
#             i += 1
#         return res

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
# leetcode submit region end(Prohibit modification and deletion)
