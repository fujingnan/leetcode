# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。 
# 
#  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。 
# 
#  示例 1： 
# 
#  输入：n = 2
# 输出：2
#  
# 
#  示例 2： 
# 
#  输入：n = 7
# 输出：21
#  
# 
#  示例 3： 
# 
#  输入：n = 0
# 输出：1 
# 
#  提示： 
# 
#  
#  0 <= n <= 100 
#  
# 
#  注意：本题与主站 70 题相同：https://leetcode-cn.com/problems/climbing-stairs/ 
# 
#  
#  Related Topics 递归 
#  👍 96 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
利用滚动数组，需要注意的是，数组是从0开始的，因此假设n取3，那么数组的坐标应当能够到达3，即len(dp)==4
T: O(N)
S: O(1)
"""
class Solution:
    def numWays(self, n: int) -> int:
        ways_flog = [1, 1, 2]
        for i in range(3, n+1):
            ways_flog[i % 3] = (ways_flog[(i-1) % 3] + ways_flog[(i-2) % 3]) % 1000000007
        return ways_flog[n % 3]
# class Solution:
#     def numWays(self, n: int) -> int:
#         if n in [0, 1]: return 1
#         if n == 2: return 2
#         ways_flog = [0] * (n+1)
#         ways_flog[0], ways_flog[1], ways_flog[2] = 1, 1, 2
#         for i in range(3, n+1):
#             ways_flog[i] = (ways_flog[i-1] + ways_flog[i-2]) % 1000000007
#         return ways_flog[-1]

# leetcode submit region end(Prohibit modification and deletion)
