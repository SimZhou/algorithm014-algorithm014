import numpy

a = numpy.random.randint(0,100,100)

def mergeSort(nums):
    '''归并先分再并'''
    if len(nums) <= 1: return nums
    mid = len(nums) // 2
    l = mergeSort(nums[:mid])
    r = mergeSort(nums[mid:])
    return merge(l, r)

def merge(a1, a2):
    res, p1, p2 = [], 0, 0
    while p1 < len(a1) and p2 < len(a2):
        if a1[p1] <= a2[p2]:
            res.append(a1[p1])
            p1 += 1
        else:
            res.append(a2[p2])
            p2 += 1
    res.extend(a1[p1:])
    res.extend(a2[p2:])
    return res
    
if __name__ == "__main__":
    print(a)
    a = mergeSort(a)
    print(a)
    # print(merge([1,2,3], [2,3,4]))