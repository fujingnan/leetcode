# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。 
# 
#  
#  
#  每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[["Q"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 9 
#  皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。 
#  
#  
#  
#  Related Topics 回溯算法 
#  👍 720 👎 0

"""
DFS
位运算
"""
# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         if n < 1: return 0
#         record = n * [0]
#         res = []
#         def is_valid(record, i, j):
#             for k in range(i):
#                 if record[k] == j or abs(k - i) == abs(record[k] - j):
#                     return False
#             return True
#
#         def dfs(record, i, n):
#             if i == n:
#                 res.append(["." * i + "Q" + "." * (n - 1 - i) for i in record])
#                 return 1
#             ways = 0
#             for j in range(n):
#                 if is_valid(record, i, j):
#                     record[i] = j
#                     ways += dfs(record, i + 1, n)
#             return ways
#         ways = dfs(record, 0, n)
#
#         return res

# class Solution:
#     def solveNQueens(selfself, n: int) -> List[List[str]]:
#         stack, res = [[(0, i)] for i in range(n)], []
#         while stack:
#             board = stack.pop()
#             row = len(board)
#             if row == n:
#                 res.append([''.join('Q' if i == c else '.' for i in range(n))
#                             for r, c in board])
#             for col in range(n):
#                 if all(col != c and abs(row - r) != abs(col - c) for r, c in board):
#                     stack.append(board + [(row, col)])
#         return res
class Solution:
    def solveNQueens(selfself, n: int) -> List[List[str]]:
        res = []
        def dfs(record, pd, nd):
            r = len(record)
            if r == n:
                res.append(record)
                return
            for c in range(n):
                if not (c in record or c-r in pd or c+r in nd):
                    dfs(record + [c], pd | {c - r}, nd | {c + r})
        dfs([], set(), set())
        print(res)
        return [[f"{'.' * way}Q{'.' * (n - way - 1)}" for way in ways] for ways in res]

# leetcode submit region end(Prohibit modification and deletion)
