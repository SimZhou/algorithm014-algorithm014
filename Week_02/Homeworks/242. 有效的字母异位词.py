# https://leetcode-cn.com/problems/valid-anagram/

# 暴力法1：sort后比较是否相等，时间O(nlogn)，空间O(1)
# 暴力法2：Counter计数后查看计数器是否相等，时间O(n)，空间O(1)，需要一点儿空间，但总的来说只需26个字母和一些整型

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 自己写hashmap
        a, b = collections.defaultdict(int), collections.defaultdict(int)
        for i in s: a[i] += 1
        for i in t: b[i] += 1
        return a == b
    
        # # 暴力法2
        # return collections.Counter(s) == collections.Counter(t)
        
        # # 暴力法1
        # return sorted(s) == sorted(t)