# https://leetcode-cn.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        for loop version
        '''
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[zero] != 0:
                zero += 1
            elif nums[i] != 0 and nums[zero] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            elif nums[i] == 0:
                pass
                
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
        
#         双指针
#         注：如果不用双指针，则任何一个原地排序算法都可以应用到这里
#         pop+append 其实和 冒泡，插入挪数据都是一个道理
#         """
#         i, j = 0, 0     # i指向0元素，j指向非零元素
#         while j <= len(nums)-1:
#             if nums[i] == 0 and nums[j] == 0: 
#                 j += 1  # i,j通时找到0，则i保持指向0元素，j往后去查找非0元素
#             elif nums[i] == 0 and nums[j] != 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#                 j += 1  # i找到0，j找到非零，则交换两者位置，然后i，j分别+1
#             elif nums[i] != 0 and nums[j] != 0:
#                 i += 1  
#                 j += 1  # i，j都找到非0，两个都+1继续搜索
#             else:
#                 print("error!")