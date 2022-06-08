# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [10,2]
# 输出: "102" 
# 
#  示例 2: 
# 
#  输入: [3,30,34,5,9]
# 输出: "3033459" 
# 
#  
# 
#  提示: 
# 
#  
#  0 < nums.length <= 100 
#  
# 
#  说明: 
# 
#  
#  输出结果可能非常大，所以你需要返回一个字符串而不是整数 
#  拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0 
#  
#  Related Topics 排序 
#  👍 134 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
利用快排的思想，将排序规则改变一下，但是核心思想还是一样的：
1. 维护两个指针记为left和right，分别从数组最左与最右开始遍历：
（1）左边数组每遍历到一个数，将该数与数组第一个数正反相拼接，如果该数拼首数小于首数拼该数，则符合
    要求，left继续往右走；感官上，如果left遍历的每个正拼与反拼进行排序，left始终需要维持着递减
    的抽象空间几何，想象成一个开口向左的大喇叭；如果遍历到不符合要求，left停止，right开始向左
    运动；
（2）与（1）相反，right始终维持着一个开口向右的大喇叭型的抽象空间几何，当遍历到不符合要求，停止，
    这时左右指针都遍历了一次，交换两指针对应位置的值，这样一来，就能保证两指针在遍历到不符合要求
    的位置，又继续符合要求而继续遍历；因为left指针希望递减，right希望递增，各自不符合要求又说
    明对彼此符合要求；
（3）遍历到最后，两指针必然相遇，相遇处的位置的值必然符合left的要求，因为严格先执行（1），再执行
    （2），此时有两种情况，第一种是left遍历到相遇，而right停止的位置时不符合right的要求的，
    不符合right的要求是因为发生了递增，相对left来说，就是递减；第二种是right遍历到相遇，由于在
    left遇到不符合要求时，已经将不符合要求的值与right交换了，因此此时righ遍历到的又是right不符
    合要求的，而相对于left来说，是符合要求的；综上，相遇时总是符合left要求的。
（4）left处的值为left维护的left以左的数组的递减的终点，因此（3）结束后，将left处的值与数组最左端
    的值交换；利用递归重复上述过程，直到每次以（0，left-1）和（left+1，arr.len）为区间的数组中
    都保持最左为正拼反拼中最小，最右为正拼反拼中最大为止

T: O(N*logN)
S: O(1)
"""
class Solution:

    def minNumber(self, nums: List[int]) -> str:
        if len(nums) == 1: return str(nums[0])
        def fast_sort(l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while nums[j] + nums[l] >= nums[l] + nums[j] and i < j: j -= 1
                while nums[i] + nums[l] <= nums[l] + nums[i] and i < j: i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[i], nums[l] = nums[l], nums[i]
            fast_sort(l, i - 1)
            fast_sort(i + 1, r)

        nums = [str(num) for num in nums]
        fast_sort(0, len(nums) - 1)
        return ''.join(nums)
# leetcode submit region end(Prohibit modification and deletion)
