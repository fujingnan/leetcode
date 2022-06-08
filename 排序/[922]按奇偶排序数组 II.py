# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。 
# 
#  对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。 
# 
#  你可以返回任何满足上述条件的数组作为答案。 
# 
#  
# 
#  示例： 
# 
#  输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length <= 20000 
#  A.length % 2 == 0 
#  0 <= A[i] <= 1000 
#  
# 
#  
#  Related Topics 排序 数组 
#  👍 186 👎 0

"""
利用哈希表：
1. 构造一个哈希表，key只有0和1，分别存放偶数和奇数；
2. 遍历原数组，奇数放在key=1，偶数放在key=0；
3. 由于题目没对各奇偶数的排列顺序做要求，所以只要将哈希表中奇偶数交错的放在结果数组中即可
T: O(N)
S: O(N)
"""

# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def sortArrayByParityII(self, A: List[int]) -> List[int]:
#         dicts = {}
#         for i in range(len(A)):
#             dicts.setdefault(A[i] % 2, []).append(A[i])
#         return [dicts[i % 2].pop() for i in range(len(A))]
"""
利用双指针：维护i和j两个变量分别代表偶数和奇数下标，两个指针每次只要移动，就移动2步。
1. 如果偶数下标的当前值为奇数，则奇数指针往前移动，直到遇到偶数值为止，交换偶数下标
   的当前值与奇数下标的当前值；
2. 如果偶数下标的当前值为偶数，偶数指针前移，奇数指针不动；
T: O(N)
S: O(1)
"""
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i, j = 0, 1
        while i < len(A):
            if not A[i] % 2 == 0:
                while not A[j] % 2 == 0 and j < len(A):
                    j += 2
                A[i], A[j] = A[j], A[i]
            i += 2
        return A
# leetcode submit region end(Prohibit modification and deletion)
