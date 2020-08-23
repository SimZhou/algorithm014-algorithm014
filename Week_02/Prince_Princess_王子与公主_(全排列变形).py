'''
很久之前，有个国王有三（n）个女儿。
有三（n）位王子来求婚，每位王子只能且必定娶到一个公主，
国王有权选择哪个女儿嫁给哪个王子，国王让他们按对每个公主的喜欢程度给出彩礼数，

请写一个全遍历计算函数，并在main函数中调用，
通过输入(通过代码定义即可)每位王子对每个公主的彩礼数，遍历所有嫁女的组合，
计算出国王如何嫁女儿可以获得最大的彩礼数，并将结果打印出来。
使用递归方式解题更好。能对n求解更好
'''

from typing import List

class Solution:
    def maxGift(self, n: int, giftTable: List[List[int]]) -> "所有可能情况":
        '''
        对于n=3来说，第1个公主位置有3种选法：[0],[1],[2]，第二个有2种，第三个有1种。
        '''
        res = []
        self._dfs(n, giftTable, res, [])
        return res

    def _dfs(self, n, giftTable, res, path):
        # Terminator
        if len(path) == n:
            res.append([path.copy(), sum([giftTable[p][i]
                                          for p, i in zip(path, range(n))])])
            return

        # Process
        for i in range(n):
            if i in path: continue  # 剪枝
            path.append(i)
            self._dfs(n, giftTable, res, path)
            path.remove(i)


if __name__ == "__main__":
    n = 4
    giftTable = [
        [2, 2, 3, 8],    # 王子1
        [3, 2, 7, 2],    # 王子2
        [5, 2, 3, 2],    # 王子3
        [5, 3, 7, 2]     # 王子4
    ]

    print(Solution().maxGift(n, giftTable))
