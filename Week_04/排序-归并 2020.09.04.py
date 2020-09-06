import numpy

a = numpy.random.randint(0,100,100)

def mergeSort(nums):
    '''归并先分再并'''
    if len(nums) <= 1: 
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)

def merge(nums1, nums2):
    res, i, j = [], 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    res.extend(nums1[i:])
    res.extend(nums2[j:])
    return res
    
if __name__ == "__main__":
    print(a)
    a = mergeSort(a)
    print(a)
    # print(merge([1,2,3], [2,3,4]))