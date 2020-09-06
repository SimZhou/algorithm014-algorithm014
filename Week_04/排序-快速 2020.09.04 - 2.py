import numpy

a = numpy.random.randint(0,100,100)

def quickSort(nums, l, r):
    if l < r:
        mid = partition(nums, l, r)
        quickSort(nums, l, mid-1)
        quickSort(nums, mid+1, r)
    return nums

def partition(nums, l, r):
    pivot = nums[r]
    while l != r:
        while l < r and nums[l] <= pivot:
            l += 1
        nums[r] = nums[l]
        while l < r and nums[r] >= pivot:
            r -= 1
        nums[l] = nums[r]
    nums[l] = pivot
    return l

    
if __name__ == "__main__":
    quickSort(a, 0, len(a)-1)
    print(a)