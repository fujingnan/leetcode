# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位
# 。 
# 
#  返回滑动窗口中的最大值。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1], k = 1
# 输出：[1]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,-1], k = 1
# 输出：[1,-1]
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [9,11], k = 2
# 输出：[11]
#  
# 
#  示例 5： 
# 
#  
# 输入：nums = [4,-2], k = 2
# 输出：[4] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  -104 <= nums[i] <= 104 
#  1 <= k <= nums.length 
#  
#  Related Topics 堆 Sliding Window
#  👍 807 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

"""
利用双端队列
"""
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         import collections
#         if len(nums) < 2: return nums
#         res = []
#         queue = collections.deque()
#         for i, v in enumerate(nums):
#             while queue and v > nums[queue[-1]]:
#                 queue.pop()
#             queue.append(i)
#             if queue[0] <= i - k:
#                 queue.popleft()
#             if i + 1 >= k:
#                 res.append(nums[queue[0]])
#         return res

"""
利用大根堆（优先队列）
"""
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if len(nums) < 2: return nums
#         import heapq
#         res, n = [], len(nums)
#         queue = [(-v, i) for i, v in enumerate(nums[:k])]
#         heapq.heapify(queue)
#         res.append(-queue[0][0])
#         for i in range(k, n):
#             heapq.heappush(queue, (-nums[i], i))
#             while queue and queue[0][1] <= i - k:
#                 heapq.heappop(queue)
#             res.append(-queue[0][0])
#         return res
#

"""
利用链表实现双端队列（不使用内置函数实现）
"""
class LinkNode:
    def __init__(self, val=0):
        self.next = None
        self.prev = None
        self.val = val


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return nums

        head = LinkNode()
        tail = LinkNode()
        head.next = tail
        tail.prev = head

        def add_node_to_tail(node):
            node.next = tail
            node.prev = tail.prev
            tail.prev.next = node
            tail.prev = node

        def remove_node_from_head():
            head.next.next.prev = head
            head.next = head.next.next

        def remove_node_from_tail():
            tail.prev.prev.next = tail
            tail.prev = tail.prev.prev

        def get_last_node():
            node = tail.prev
            return node

        def get_first_node():
            node = head.next
            return node

        res, n = [], len(nums)
        for i in range(0, n):
            while tail.prev.prev and nums[i] > nums[get_last_node().val]:
                remove_node_from_tail()
            add_node_to_tail(LinkNode(i))
            if get_first_node().val <= i-k:
                remove_node_from_head()
            if i + 1 >= k:
                res.append(nums[get_first_node().val])
        return res

# leetcode submit region end(Prohibit modification and deletion)
