# 第4周学习笔记

坚持就是胜利！



## 刷题记录

额外刷题，来自LC日推题，群内每日一题，随性刷题等

| #    | 题目名                                                       | 难度  | 关键词               | 已过遍数 |
| ---- | ------------------------------------------------------------ | ----- | -------------------- | -------- |
| 31   | [下一个排列](https://leetcode-cn.com/problems/next-permutation/) | 💛中等 | 数组                 | 1        |
| 60   | [第k个排列](https://leetcode-cn.com/problems/permutation-sequence/) | 💛中等 | 数学，回溯           | 1        |
| 53   | [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/) | 💚简单 | 数组，分治，动态规划 | 1        |
|      |                                                              |       |                      |          |

实践题

| #    | 题目名                                                       | 难度  | 关键词                  | 已过遍数 |
| ---- | ------------------------------------------------------------ | ----- | ----------------------- | -------- |
| 102  | [二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/#/description) | 💚简单 | 树，BFS                 | 2        |
|      | [最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/#/description) |       |                         |          |
| 22   | [括号生成](https://leetcode-cn.com/problems/generate-parentheses/#/description) | 💛中等 | 字符串，回溯            | 2        |
|      | [在每个树行中找最大值](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/#/description) |       |                         |          |
|      | [零钱兑换](https://leetcode-cn.com/problems/coin-change/)    | 💛中等 | <u>贪心法的反例</u>，DP |          |
| 69   | [x 的平方根](https://leetcode-cn.com/problems/sqrtx/)        | 💚简单 | 数学，二分查找          | 2        |
|      | [有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square/) |       |                         |          |

作业题

| #    | 题目名                                                       | 难度  | 关键词           | 已过遍数 |
| ---- | ------------------------------------------------------------ | ----- | ---------------- | -------- |
| 860  | [柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/description/) | 💚简单 | 贪心算法         | 2        |
| 122  | [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/) | 💚简单 | 贪心算法，数组   | 3        |
| 455  | [分发饼干](https://leetcode-cn.com/problems/assign-cookies/description/) | 💚简单 | 贪心算法         | 2        |
| 874  | [模拟行走机器人](https://leetcode-cn.com/problems/walking-robot-simulation/description/) | 💚简单 | 贪心             | 1        |
|      | 使用二分查找，寻找半有序数组<br/>[4, 5, 6, 7, 0, 1, 2] 中间无序的地方 |       |                  |          |
|      | [单词接龙](https://leetcode-cn.com/problems/word-ladder/description/) |       |                  |          |
| 200  | [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/) | 💛中等 | DFS，BFS，并查集 | 2        |
|      | [扫雷游戏](https://leetcode-cn.com/problems/minesweeper/description/) |       |                  |          |
| 55   | [跳跃游戏](https://leetcode-cn.com/problems/jump-game/)      | 💛中等 | 贪心算法，数组   | 1        |
| 33   | [搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/) | 💛中等 | 数组，二分       | 1        |
|      | [搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/) |       |                  |          |
|      | [寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/) |       |                  |          |
|      | [单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/description/) |       |                  |          |
|      | [跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii/) |       |                  |          |



## 视频笔记

### 1. DFS, BFS

DFS和BFS是针对树/图结构来讲的。

二叉树DFS模板：

```python
def dfs(node):
    if node in visited:
        return
   	visited.add(node)
    	
    dfs(node.left)
    dfs(node.right)
```

多叉树DFS模板：

```python
visited = set()
def dfs(node, visited):
    visited.add(node)
    # process current node here
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
```

对比一下，判断是否访问过的位置不同（一个在最开始，一个在深入递归时），但本质是一样的。

BFS模板：

```python
def bfs(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```

[DFS 代码模板（递归写法、非递归写法）](https://shimo.im/docs/UdY2UUKtliYXmk8t/)

[BFS 代码模板](https://shimo.im/docs/ZBghMEZWix0Lc2jQ/)

### 2. 贪心算法

贪心算法：一种在**每一步选择中**都**采取在当前状态下最好或最优**（最有利）的选择，从而希望导致结果是全局最好或者最优的算法。

贪心算法和动态规划的区别在于动态规划可以回退，而贪心算法不能回退。

[动态规划定义](https://zh.wikipedia.org/wiki/动态规划)

### 3. 二分查找

※ 二分查找的前提

- 目标函数单调性（单调递增/递减）
- 存在上下界（bounded）
- 能够通过索引访问（index accessible）（比如链表就不行）

```python
left, right = 0, len(array) - 1
while left <= right:
    mid = (left + right) / 2
    if array[mid] == target:
        # find the target
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```



[二分查找代码模板](https://shimo.im/docs/xvIIfeEzWYEUdBPD/)

[Fast InvSqrt() 扩展阅读](https://www.beyond3d.com/content/articles/8/)



## 使用二分查找，寻找一个半有序数组[4, 5, 6, 7, 0, 1, 2] 中间无序的地方

