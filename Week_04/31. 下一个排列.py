# https://leetcode-cn.com/problems/next-permutation/

## 字典序算法
# 1. 从右往左，查找第一个左邻小于自身的左邻位置i （若未找到，则已是最后一个排列，返回reversed()）
# 2. 从右往左，查找第一个比左邻大的元素位置j
# 3. 交换i, j两者的值
# 4. 将i后面的所有值反转

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]: break
        else:
            nums[:] = nums[::-1]
            return
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > nums[i]: break
        nums[j], nums[i] = nums[i], nums[j]
        nums[i+1:] = reversed(nums[i+1:])