import numpy

a = numpy.random.randint(0,100,100)

def quickSort(nums, l, r):
    '''快排先partition再分'''
    if l >= r: return
    pivot, lt, rt = nums[r], l, r
    while l < r:
        while l < r and nums[l] <= pivot:
            l += 1
        nums[r] = nums[l]
        while l < r and nums[r] >= pivot:
            r -= 1
        nums[l] = nums[r]
    nums[l] = pivot
    quickSort(nums, lt, l-1)
    quickSort(nums, l+1, rt)
        
if __name__ == "__main__":
    quickSort(a, 0, len(a)-1)
    print(a)