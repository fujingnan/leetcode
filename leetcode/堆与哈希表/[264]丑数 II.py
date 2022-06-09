# 编写一个程序，找出第 n 个丑数。 
# 
#  丑数就是质因数只包含 2, 3, 5 的正整数。 
# 
#  示例: 
# 
#  输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。 
# 
#  说明: 
# 
#  
#  1 是丑数。 
#  n 不超过1690。 
#  
#  Related Topics 堆 数学 动态规划 
#  👍 461 👎 0

# leetcode submit region begin(Prohibit modification and deletion)
"""
动态规划：
1. 第一个丑数为1，接下来就是依次乘2、乘3，乘5，并取三个乘积中最小的数作为第二个丑数；
2. 再将第二个丑数依次乘2、乘3，乘5，并取三个乘积中最小的数作为第三个丑数；
3. 以此类推……
T: O(N)
S: O(N)
"""
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         dp, u2, u3, u5 = [1] * n, 0, 0, 0
#         for i in range(1, n):
#             p2, p3, p5 = dp[u2] * 2, dp[u3] * 3, dp[u5] * 5
#             new_u = min(p2, min(p3, p5))
#             dp[i] = new_u
#             if new_u == p2: u2 += 1
#             if new_u == p3: u3 += 1
#             if new_u == p5: u5 += 1
#         return dp[-1]
"""
小根堆：
1. 将1放入堆ls中
2. 遍历n次
3. 取出堆顶元素cur，放入res列表中
4. cur乘以2,3,5分别得到cur1，cur2，cur3,
5. 将{cur1,cur2,cur3}与{ls}求差集，将差集元素放入堆中

T: O(N*logN)
S: O(N)
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq
        lq, res = [1], []
        heapq.heapify(lq)
        for _ in range(n):
            cur = heapq.heappop(lq)
            res.append(cur)
            cur2, cur3, cur5 = cur * 2, cur * 3, cur * 5
            temp = {cur2, cur3, cur5} - set(lq)
            if temp:
                for i in temp:
                    heapq.heappush(lq, i)
        return res[-1]


# leetcode submit region end(Prohibit modification and deletion)
