# https://leetcode-cn.com/problems/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 倒序排序
        i, j, k = len(nums1)-1, m-1, n-1
        while j+1 and k+1:
            if nums1[j] < nums2[k]:
                nums1[i] = nums2[k]
                k -= 1
            else:
                nums1[i] = nums1[j]
                j -= 1
            i -= 1
        nums1[:k+1] = nums2[:k+1]
                
        # # 归并排序的归并 O(m+n), O(m+n)
        # i, j = 0, 0
        # res = []
        # while i < m and j < n:
        #     if nums1[i] <= nums2[j]:
        #         res.append(nums1[i])
        #         i += 1
        #     else:
        #         res.append(nums2[j])
        #         j += 1
        # res.extend(nums1[i:m])
        # res.extend(nums2[j:n])
        # nums1[:] = res
        
        # # 合并后排序 O((m+n)log(m+n)), O(1)
        # # 注意python中
        # nums1[:] = sorted(nums1[:m] + nums2)
        # return nums1
        