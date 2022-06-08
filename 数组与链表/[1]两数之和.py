# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 103 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  只会存在一个有效答案 
#  
#  Related Topics 数组 哈希表 
#  👍 10426 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
排序+双指针
T: O(N*logN)
S: O(N)
"""
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         maps = [(v, i) for i, v in enumerate(nums)]
#         maps.sort()
#         l, r = 0, len(maps) - 1
#         while l < r:
#             if maps[l][0] + maps[r][0] == target:
#                 return [maps[l][1], maps[r][1]]
#             elif maps[l][0] + maps[r][0] > target:
#                 r -= 1
#             else:
#                 l += 1
"""
哈希表: 遍历数组中的每一个元素，并取到目标值减去该元素后的剩下值存入键，这个剩下值即对应数组中
每一个元素对应的目标值所需的另一个加数，也就是说，遍历一个数，看看该数是否能与之前的数相加等于
目标值
T: O(N)
S: O(N)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, v in enumerate(nums):
            res = target - v
            if v in d:
                return [d[v], i]
            else:
                d[res] = i
# leetcode submit region end(Prohibit modification and deletion)
