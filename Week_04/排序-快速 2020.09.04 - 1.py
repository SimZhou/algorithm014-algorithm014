import numpy, time
rint = lambda x: numpy.random.randint(0,100,x)

def quickSort(nums, l, r):
    if l >= r: return                                         # 错误点1，l，r可能越界，所以要判断 l >= r
    ltemp, rtemp = l, r
    p = nums[r]                                               # 错误点4，要设置为输入的最后一维而不是nums
    while l != r:                                             
        time.sleep(0.5)
        while l < r and nums[l] <= p:                         # 错误点2：需要找的是左边第一个 大于 p的数，因此是<=p
            l += 1
            print(ltemp, rtemp, l, r, nums, '+')
        nums[r]= nums[l]
        while l < r and nums[r] >= p:                         # 错误点3：同错误点2
            r -= 1
            print(ltemp, rtemp, l, r, nums, '-')
        nums[l] = nums[r]
        print(ltemp, rtemp, l, r, nums)
    nums[l] = p
    quickSort(nums, ltemp, r-1)
    quickSort(nums, r+1, rtemp)

'''Write it again'''
def quicks(nums, l, r):
    if l >= r: return
    ltemp, rtemp = l, r
    pivot = nums[l]
    while l != r:
        while l < r and nums[r] >= pivot:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] <= pivot:
            l += 1
        nums[r] = nums[l]
    nums[l] = pivot
    quicks(nums, ltemp, l-1)
    quicks(nums, l+1, rtemp)

if __name__ == "__main__":
    # quickSort(a, 0, len(a)-1)
    # quickSort([19, 73, 54, 29, 54, 65, 99, 90, 49, 77], 0, 9)
    # quickSort([19,29], 0, 1)
    a = rint(50)
    quicks(a, 0, len(a)-1)
    print(a)