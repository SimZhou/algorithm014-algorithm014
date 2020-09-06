import numpy

a = numpy.random.randint(0,100,100)

def mergeSort(nums):
    if len(nums) <= 1: return nums
    m = len(nums) // 2
    l = mergeSort(nums[:m])
    r = mergeSort(nums[m:])
    return merge(l, r)

def merge(na, nb):
    res, i, j = [], 0, 0
    while i < len(na) and j < len(nb):
        if na[i] <= nb[j]:
            res.append(na[i])
            i += 1
        else:
            res.append(nb[j])
            j += 1
    res.extend(na[i:])
    res.extend(nb[j:])
    return res
    
    
if __name__ == "__main__":
    print(a)
    a = mergeSort(a)
    print(a)
    # print(merge([1,2,3], [2,3,4]))