import numpy

a = numpy.random.randint(0,100,100)

def bubble(nums):
    '''n^2, 稳定。每次把大的元素冒到最后面。'''
    for _ in range(len(nums)-1, -1, -1):
        for i in range(_):
            if nums[i] > nums[i+1]: nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

def select(nums):
    '''n^2，不稳定。每次从i+1到len(nums)中选一个比i小的，与之交换。'''
    minIndex = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[j] < nums[minIndex]: minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums

def insertion(nums):
    '''n^2，稳定。就像理牌，每次从右边堆中选一个，找到左边堆中的插入位置，进行插入。它相当于是选择排序的反面。'''
    for i in range(1, len(nums)):
        pivot = nums[i]
        while i > 0 and nums[i-1] > pivot:
            nums[i] = nums[i-1]; i -= 1
        nums[i] = pivot
    return nums

if __name__ == "__main__":
    print(a)
    # bubble(a)
    # select(a)
    insertion(a)
    print(a)
    # print(merge([1,2,3], [2,3,4]))