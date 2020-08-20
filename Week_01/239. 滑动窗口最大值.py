# https://leetcode-cn.com/problems/sliding-window-maximum/

# 暴力法：O(kn)
# 堆heap：O(nlogk), O(k)
# 单调队列：O(n), O(k)

class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     '''
    #     暴力法,oKN 超时了
    #     '''
    #     res = []
    #     for i in range(len(nums)-k+1):
    #         res.append(max(nums[i:i+k]))
    #     return res
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        更简洁的
        '''
        res, q = [], collections.deque()
        for i in range(len(nums)):
            if q and q[0][0] <= i - k: q.popleft()
            while q and nums[i] > q[-1][1]:
                q.pop()
            # 只要栈为空或者当前数小于栈中数，则往里添加
            q.append((i, nums[i]))
            res.append(q[0][1])
        return res[k-1:]
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        单调队列，插入元素时只插入比当前当前队列中最后一个元素更大的元素 《——错误
        应该用单调递减栈，最大元素总在最左边
        这样的栈满足了堆无法满足的一个条件：它是当前窗口中最大以及最左边的元素。
        '''
        res, q = [], []
        q.append((-1, float("inf")))  # 哨兵元素，避免判空
        for i in range(k):
            while q[-1][1] < nums[i]: q.pop()
            q.append((i, nums[i]))
            # print(q)
        res.append(q[1][1])
        for i in range(k, len(nums)):
            if i - q[1][0] >= k : q.pop(1)
            while q[-1][1] < nums[i]: q.pop()
            q.append((i, nums[i]))
            # print(q)
            res.append(q[1][1])
        return res