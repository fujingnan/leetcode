# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下： 
# 
#  
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1. 
# 
#  斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。 
# 
#  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 2
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 5
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 100 
#  
#  Related Topics 递归
#  👍 82 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1: return n
#         fi = [0] * (n + 1)
#         fi[0], fi[1] = 0, 1
#         for i in range(2, n + 1):
#             fi[i] = (fi[i-1] + fi[i-2]) % 1000000007
#         return fi[i]

# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1: return n
#         fi = [0, 1]
#         for i in range(2, n + 1):
#             fi[i % 2] = (fi[(i-1) % 2] + fi[(i-2) % 2]) % 1000000007
#         return fi[n % 2]

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        pre, cur = 0, 1
        for i in range(2, n+1):
            pre, cur = cur % 1000000007, (pre + cur) % 1000000007
        return cur
# leetcode submit region end(Prohibit modification and deletion)
