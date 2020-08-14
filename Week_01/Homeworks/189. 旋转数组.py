# https://leetcode-cn.com/problems/rotate-array/

# 1.一个个pop，然后加到左边。时间kn，空间1
# 2.一次性popk个，然后加到左边。时间：n，空间：k
# 3.队列，时间：n+k，空间：n
# 4.环状替换，把每个元素直接替换到应该到的位置上去，使用一个temp缓存值     On, O1
# 5.反转+反转      On, O1
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # 3次反转
        n = len(nums)
        k = k % n
        nums[:n-k], nums[n-k:] = reversed(nums[:n-k]), reversed(nums[n-k:])
        nums.reverse()
        
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # 环状替换
#         n = len(nums)
#         count = n
#         start = 0
#         while count:
#             ind = start
#             temp = nums[ind]

#             for _ in range(n):
#                 new_ind = (ind+k) % n
#                 temp, nums[new_ind] = nums[new_ind], temp
#                 ind = new_ind
#                 count -= 1
#                 if ind == start: break
#             start += 1