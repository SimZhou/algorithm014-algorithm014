# https://leetcode-cn.com/problems/group-anagrams/

# 排序哈希表法：把每个字符串排序后的hash值作为value存入hash表，原输入作为key。
# 时间 nklogk，空间 n

# 不排序哈希表法：
# 时间 nk，空间 n

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 不排序，直接拿ord之和当作哈希
        hashMap = collections.defaultdict(list)
        for word in strs:
            val = [0] * 26
            for char in word:
                val[ord(char) - ord("a")] += 1
            hashMap[tuple(val)].append(word)
        return list(hashMap.values())
        
        # # 哈希表法
        # dct = collections.defaultdict(list)
        # for i in strs:
        #     dct[hash("".join(sorted(i)))].append(i)
        # return list(dct.values())