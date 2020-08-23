# https://leetcode-cn.com/problems/top-k-frequent-elements/

# 1. 哈希表，然后排序：时间O(n+mlogm)，空间O(m)，m为元素类别数目
# 2. 一遍扫描计数，然后把计数全部丢进大顶堆里，然后取topK个。时间：O(n+nlogn)，空间：O(n)
#       不不不这是不正确的
#       维护一个元素个数为k的小顶堆就行了，只要当前元素比堆顶元素大，就拿出堆顶，然后放进去
#       这样一来，在里面的就是TopK
# 3. 桶排序O(n)+O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 桶排序
        hashTable = collections.defaultdict(int)
        for i in nums: hashTable[i] += 1        
        
        bucket = [[] for i in range(len(nums)+1)]
        for i, count in hashTable.items():
            bucket[count].append(i)
        
        res = [j for i in bucket[::-1] if i for j in i][:k]
        return res
        
        # # 哈希表+TopK堆
        # hashTable = collections.defaultdict(int)
        # for i in nums: hashTable[i] += 1
        # # TopK heap
        # TopK = []
        # for i, count in hashTable.items():
        #     if len(TopK) < k: heapq.heappush(TopK, (count, i))
        #     else: 
        #         if TopK[0][0] < count: heapq.heapreplace(TopK, (count, i))
        # return [i[1] for i in TopK]
        
        # # 哈希表+归并排序/快排
        # hashTable = collections.defaultdict(int)
        # for i in nums:
        #     hashTable[i] += 1
        # return [i for i, j in sorted(hashTable.items(), key = lambda x: x[1], reverse = True)][:k]