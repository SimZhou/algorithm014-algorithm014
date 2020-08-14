# https://leetcode-cn.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums):
        '''
        3. 龟兔赛跑-佛洛依德算法
        复杂度：O(n)
        把下标看成值，实际值看成指针，则数组就是一个链表，
        如果数组中有重复值，则代表有指针重复指向同一个元素
        问题转化为找链表入口点的问题。
        '''
        t, h = nums[0], nums[0]
        while 1:
            t = nums[t]
            h = nums[nums[h]]
            if t == h: break
        i = nums[0]
        while i != h:
            i = nums[i]
            h = nums[h]
        return i
            
        
        # '''
        # 2. 排序后查找
        # 先排序，然后顺序查找一遍
        # 复杂度：O(nlogn+n)
        # '''
        # nums = sorted(nums)
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return nums[i]

    # def findDuplicate(self, nums: List[int]) -> int:
    #     '''
    #     1. 暴力法 - 超时
    #           超时例子: [3813,8229,15919,16146,19061,26146,11849,28124,22288,19711,6050,27586,25607,4226,16366,28307,19954,6764,27118,17464,21581,662...
    #     '''
    #     for i in range(len(nums)-1):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] == nums[j]: return nums[i]