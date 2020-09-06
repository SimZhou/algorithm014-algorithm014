# https://leetcode-cn.com/problems/n-queens/

# N皇后问题。
# 这个问题的关键是如何用回溯的思想来考虑它。也就是转换为全排列的问题。

# 首先，n个皇后在nxn的棋盘上面，有(nxn)(nxn-1)...(nxn-n)种排列方式。(其中有一些是相同的，但是顺序不同，并且他们都可以是n皇后的解)

# 所以问题就变成了如何通过剪枝的手段来寻找解的问题。

# 当放置完一个皇后后，其横纵斜3个方向上都不能再放置新的皇后，所以很自然就可以想到使用一个二维表来储存可访问节点。

# 那么如何在放置完一个棋子后，对其表结构填充呢？首先，横向和纵向很好做，只需要把放置位置(i, j)所对应的四个方向延申进行填充即可。斜向怎么办呢？其实也不难，通过公式来做就行。


# 这道题目还有一个难点，就是它需要你返回所有不重复的解，因此，在求解过程中进行剪枝，也非常重要了


# -------

# 查看到了国际版答案，判断有效的逻辑非常给力：

# 若一个点(i, j)被选取，那么代表所有x=i或者y=j的点都不再能被选取，另外对角线怎么办呢？
# 既然是对角线，那么就会有一个一元二次方程：y=ax+b。正对角线为：y=x+b，反对角线为：y=-x+b。带入(i, j)解得：b=j-i，b=j+i。因此，只要满足y-x==j-i，y+x==j+i的点，都不再能被选取了。

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(temp, diff_set, sum_set):
            if len(temp) == n:
                res.append(temp.copy())
                return
            for i in range(n):
                if i not in temp and len(temp)-i not in diff_set and len(temp) + i not in sum_set:
                    dfs(temp+[i], diff_set.union({len(temp)-i}), sum_set.union({len(temp)+i}))
        res = []
        dfs([], set(), set())
        return [["." * i + "Q" + "." * (n-i-1) for i in ans] for ans in res]
