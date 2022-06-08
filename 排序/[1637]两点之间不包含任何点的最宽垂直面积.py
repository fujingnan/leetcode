# 给你 n 个二维平面上的点 points ，其中 points[i] = [xi, yi] ，请你返回两点之间内部不包含任何点的 最宽垂直面积 的宽度。 
# 
#  垂直面积 的定义是固定宽度，而 y 轴上无限延伸的一块区域（也就是高度为无穷大）。 最宽垂直面积 为宽度最大的一个垂直面积。 
# 
#  请注意，垂直区域 边上 的点 不在 区域内。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：points = [[8,7],[9,9],[7,4],[9,7]]
# 输出：1
# 解释：红色区域和蓝色区域都是最优区域。
#  
# 
#  示例 2： 
# 
#  
# 输入：points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == points.length 
#  2 <= n <= 105 
#  points[i].length == 2 
#  0 <= xi, yi <= 109 
#  
#  Related Topics 排序 
#  👍 6 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        if len(points) == 2: return points[1][0]-points[0][0]
        points.sort(key=lambda x: x[0], reverse=True)
        pre, maxn = points[0], 0
        for cur in points[1:]:
            maxn, pre[0] = max(maxn, pre[0] - cur[0]), cur[0]
        return maxn
# leetcode submit region end(Prohibit modification and deletion)
