import numpy

def quickSort(nums, l, r):
    if l >= r: return
    pivot = nums[l]; ltemp = l; rtemp = r;
    while l < r:
        while l < r and nums[r] >= pivot:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] <= pivot:
            l += 1
        nums[r] = nums[l]
    nums[l] = pivot
    quickSort(nums, ltemp, l-1)
    quickSort(nums, l+1, rtemp)



if __name__ == "__main__":
    a = numpy.random.randint(0,100,1000)
    quickSort(a, 0, len(a)-1)
    print(a)