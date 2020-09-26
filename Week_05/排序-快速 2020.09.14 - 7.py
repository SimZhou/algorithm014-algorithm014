import numpy

def quicks(nums, l, r):
    if l >= r: return
    pivot = nums[l]
    lt, rt = l, r
    while l < r:
        while l < r and nums[r] >= pivot:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] <= pivot:
            l += 1
        nums[r] = nums[l]
    nums[l] = pivot
    quicks(nums, lt, l-1)
    quicks(nums, l+1, rt)

if __name__ == "__main__":
    a = numpy.random.randint(0,100,1000)
    quicks(a, 0, len(a)-1)
    print(a)