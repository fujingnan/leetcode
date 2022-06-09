# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -105 <= nums[i] <= 105 
#  
#  Related Topics 数组 双指针 
#  👍 3022 👎 0

# leetcode submit region begin(Prohibit modification and deletion)
"""
利用哈希表：遍历数组，第一层循环遍历到i时，进入第二层循环，第二层循环从i+1开始，
当第二层循环遍历到的每个数都不在哈希表中，则第二层循环的每个数与第一层循环遍历到
的当前数相加（取负），作为哈希表的键。第一、二层循环的各个数相当于题目中的a、b
T: O(N^2)
S: O(N)
"""
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) < 3: return []
#         t = False
#         for p in nums:
#             if p <= 0: t = True
#         if t == False: return []
#         nums.sort()
#         res = set()
#         for i, v in enumerate(nums[:-2]):
#             if i >= 1 and v == nums[i-1]:
#                 continue
#             record = {}
#             for x in nums[i+1:]:
#                 if not x in record:
#                     record[-v-x] = None
#                 else:
#                     res.add((v, -v-x, x))
#         return list(map(list, res))
"""
双指针
T: O(N^2)
S: O(1)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
