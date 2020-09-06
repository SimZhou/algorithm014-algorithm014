# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''一遍扫描，太蠢'''
        # for i in range(len(nums)):
        #     if nums[i] == target: return i
        # else:
        #     return -1
        '''二分查找，分治'''
        '''分一半，有序的那边执行二分查找，无序的那一边继续二分'''
        '''所以需要定义一个二分查找函数'''
        def search(l, r, target):
            if l > r: return -1
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            if nums[l] == target: return l
            if nums[r] == target: return r
            if nums[l] <= nums[mid]:  # 左边有序
                if nums[l] <= target < nums[mid]:
                    return search(l, mid-1, target)
                else: 
                    return search(mid + 1, r, target)
            else:                   # 右边有序
                if nums[mid] <= target < nums[r]:
                    return search(mid + 1, r, target)
                else:
                    return search(l, mid - 1, target)
                
            
        return search(0, len(nums)-1, target)