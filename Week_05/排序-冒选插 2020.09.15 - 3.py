import numpy

a = b = c = numpy.random.randint(0,100,100)

def bubble(nums):
    '''外循环n-1~1，内循环0~i'''
    for i in range(len(nums)-1, -1, -1):
        for j in range(i):
            if nums[j] > nums[j+1]: nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def select(nums):
    '''外循环0~n-1，内循环i-n'''
    for i in range(0, len(nums)-1):
        minInd = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[minInd]: minInd = j
        nums[minInd], nums[i] = nums[i], nums[minInd]
    return nums

def insertion(nums):
    '''外循环0-n，内循环while'''
    for i in range(1, len(nums)):
        pivot = nums[i]
        while i and nums[i-1] > pivot:
            nums[i] = nums[i-1]
            i -= 1
        nums[i] = pivot
    return nums

if __name__ == "__main__":
    print(a)
    # bubble(a)
    # select(a)
    # insertion(a)
    # print(a)
    print(insertion(a) == select(b), select(b) == bubble(c))
    # print(merge([1,2,3], [2,3,4]))