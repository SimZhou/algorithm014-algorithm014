# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        双指针，要考虑2个问题：
            1. 什么时候该挪? i
            2. 该挪到什么位置? j
        '''
        i, j = 0, 0                     # 一开始都从0开始
        while i < len(nums)-1:
            if nums[i+1] == nums[i]:    # i+1的元素和i相同，说明还没到挪的时候
                i += 1                  # （因为后面可能还是相同）
            elif nums[i+1] != nums[i]:  # i+1的元素和i不同，说明到头了，该挪了
                nums[j+1] = nums[i+1]
                i += 1
                j += 1                  # 挪完，j+1肯定大于j了，所以j++
        return j + 1