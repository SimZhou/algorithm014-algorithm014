# https://leetcode-cn.com/problems/3sum

class Solution:
    # 方法1：三重循环，复杂度O(n^3)
    # 方法2：二重循环，加hashtable，复杂度(O^2)
    # 方法3：预排序+双指针，复杂度O(n^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        预排序+双指针，复杂度O(n^2)，for+while
        '''
        if len(nums) < 3: return []
        nums.sort()
        
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]: continue
            j, k = i + 1, len(nums)-1
            while j < k:
                candidate = nums[j] + nums[k]
                if j > i+1 and nums[j] == nums[j-1]: j += 1
                elif candidate < -nums[i]:
                    j += 1
                elif candidate > -nums[i]:
                    k -= 1
                elif candidate == -nums[i]:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1    # 这里注意
        return res

#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         '''
#         官方题解，两层for的预排序+双指针
#         '''
#         n = len(nums)
#         nums.sort()
#         ans = list()
        
#         # 枚举 a
#         for first in range(n):
#             # 需要和上一次枚举的数不相同
#             if first > 0 and nums[first] == nums[first - 1]:
#                 continue
#             # c 对应的指针初始指向数组的最右端
#             third = n - 1
#             target = -nums[first]
#             # 枚举 b
#             for second in range(first + 1, n):
#                 # 需要和上一次枚举的数不相同
#                 if second > first + 1 and nums[second] == nums[second - 1]:
#                     continue
#                 # 需要保证 b 的指针在 c 的指针的左侧
#                 while second < third and nums[second] + nums[third] > target:
#                     third -= 1
#                 # 如果指针重合，随着 b 后续的增加
#                 # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
#                 if second == third:
#                     break
#                 if nums[second] + nums[third] == target:
#                     ans.append([nums[first], nums[second], nums[third]])  
#         return ans
    
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         '''
#         二重循环 + hashtable + 判重，O(n^2)
#         相当于固定一个元素，求特定和的两数之和，然后遍历每个元素都做一遍同样操作
#         *超时*
#         '''
#         res = []
#         for i in range(len(nums)-2): 
#             table = set()
#             for j in range(i+1, len(nums)):
#                 if - nums[i] - nums[j] in table:
#                     if sorted([nums[i], nums[j], - nums[i] - nums[j]]) not in res:
#                         res.append(sorted([nums[i], nums[j], - nums[i] - nums[j]]))
#                 else:
#                     table.add(nums[j])
#         return res

#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         '''
#         三重循环，加判重，超时间限制
#         '''
#         res = []
#         for i in range(len(nums)-2):
#             for j in range(i+1, len(nums)-1):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         if sorted([nums[i], nums[j], nums[k]]) not in res:
#                             res.append(sorted([nums[i], nums[j], nums[k]]))
#         return res