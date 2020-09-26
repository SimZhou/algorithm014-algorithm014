# 第7周学习笔记

本周学习：

- 字典树，并查集
- 高级搜索：双向BFS，启发式搜索等
- 红黑树和AVL树



## 刷题记录

额外刷题，来自LC日推题，群内每日一题，随性刷题等

| #    | 题目名 | 难度  | 关键词                                   | 已过遍数 |
| ---- | ------ | ----- | ---------------------------------------- | -------- |
|      |        | 💚简单 | [栈](https://leetcode-cn.com/tag/stack/) |          |
|      |        |       |                                          |          |
|      |        |       |                                          |          |
|      |        |       |                                          |          |

实践题

| #    | 题目名                                                       | 难度 | 关键词 | 已过遍数 |
| ---- | ------------------------------------------------------------ | ---- | ------ | -------- |
|      | [二叉树的层次遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/) |      |        |          |
|      | [二进制矩阵中的最短路径](https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/) |      |        |          |
|      | [滑动谜题](https://leetcode-cn.com/problems/sliding-puzzle/) |      |        |          |
|      |                                                              |      |        |          |

作业题

| #    | 题目名                                                       | 难度  | 关键词       | 已过遍数 |
| ---- | ------------------------------------------------------------ | ----- | ------------ | -------- |
|      | [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)  | 💚简单 |              |          |
| 208  | [实现 Trie (前缀树) ](https://leetcode-cn.com/problems/implement-trie-prefix-tree/#/description) | 💛中等 | 设计，字典树 | 2        |
| 547  | [朋友圈](https://leetcode-cn.com/problems/friend-circles)    | 💛中等 | DFS，并查集  | 2        |
|      | [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/) | 💛中等 |              |          |
|      | [被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/) | 💛中等 |              |          |
|      | [有效的数独](https://leetcode-cn.com/problems/valid-sudoku/description/) | 💛中等 |              |          |
|      | [括号生成](https://leetcode-cn.com/problems/generate-parentheses/) | 💛中等 |              |          |
|      | [单词接龙](https://leetcode-cn.com/problems/word-ladder/)    | 💛中等 |              |          |
|      | [最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/) | 💛中等 |              |          |
|      | [单词搜索 II ](https://leetcode-cn.com/problems/word-search-ii/) | 🧡困难 |              |          |
|      | [N 皇后](https://leetcode-cn.com/problems/n-queens/)         | 🧡困难 |              |          |
|      | [解数独](https://leetcode-cn.com/problems/sudoku-solver/#/description) | 🧡困难 |              |          |



## 视频笔记

### 1. 字典树，并查集

#### 1.1 字典树

- 字典构成的树，专门用来做索引。（词项索引）

- [Trie树代码模板](https://shimo.im/docs/DP53Y6rOwN8MTCQH/read)

- **[单词搜索 II](https://leetcode-cn.com/problems/word-search-ii/) 使用Trie树实现的时间复杂度：**

假设候选列表里有n个单词，每个单词长度为m，单词矩阵长宽为x, y，则：

空间复杂度为 O(26·m) = O(m)

时间复杂度为 O(x·y·m)（最坏情况下每个位置都需要查找m次）

#### 1.2 并查集(Disjoint Set)

- 用来解决组团/配对问题
- 并查集API：
  - **makeSet(s)**：建立一个新的并查集，其中包含s个**单元素集合**。
  - **unionSet(x, y)**：把元素x和元素y所在的集合合并，要求x和y所在的集合不相交，如果相交则不合并。
  - **find(x)**：找到元素x所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。

- [并查集代码模板](https://shimo.im/docs/VtcxL0kyp04OBHak)

```python
class UnionFind:
    def __init__(self):
        # for i = 0 ... n: p[i] = i;
        self.p = [i for i in range(n)]
    def union(self, i, j):
        p1 = self.parent(i)
        p2 = self.parent(j)
        self.p[p1] = p2
    def parent(self, i):
        root = i
        while self.p[root] != root:
            root = self.p[root]
        while self.p[i] != i: # 路径压缩
            self.p[i], i = root, self.p[i]
            # x = i; i = self.p[i]; self.p[x] = root
        return root
```



### 2. 高级搜索

[DFS 代码模板](https://shimo.im/docs/UdY2UUKtliYXmk8t)，[BFS 代码模板](https://shimo.im/docs/ZBghMEZWix0Lc2jQ)，[AlphaZero Explained](https://nikcheerla.github.io/deeplearningschool/2018/01/01/AlphaZero-Explained/)，[Wikipedia - 棋类复杂度](https://en.wikipedia.org/wiki/Game_complexity)

**※ 灵感：人类做决策和机器做决策，都是靠回溯（思考多种可能性路径，选择当前最优的一步），而且AlphaGo做决策的过程也非常像人脑。因此，是否可以考虑用这个方法来实现某种强决策系统/强人工智能呢？**

#### 2.1 剪枝

例如：括号生成问题，组合问题等回溯问题，都可以利用剪枝来降低复杂度

例子：数独

#### 2.2 双向BFS

word-ladder 单词接龙



双向BFS模板：

```python

```



#### 2.3 启发式搜索

- [A* 代码模板](https://shimo.im/docs/8CzMlrcvbWwFXA8r)
- [相似度测量方法](https://dataaspirant.com/2015/04/11/five-most-popular-similarity-measures-implementation-in-python/)
- [二进制矩阵中的最短路径的 A* 解法](https://leetcode.com/problems/shortest-path-in-binary-matrix/discuss/313347/A*-search-in-Python)
- [8 puzzles 解法比较](https://zxi.mytechroad.com/blog/searching/8-puzzles-bidirectional-astar-vs-bidirectional-bfs/)

### 3. AVL树/红黑树

[维基百科：平衡树](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree)

#### 3.1 AVL树

- 以2位科学家的名字命名
- 是平衡二叉搜索树
- 每个节点均有一个平衡因子balance factor = {-1, 0, 1}
- 对应有4种旋转操作，分别是左左，右右，左右，和右左

#### 3.2 红黑树

- 近似平衡二叉树
- 能够确保任何一个节点的左右子树的**高度差小于两倍**。具体来说，红黑树是满足如下条件的二叉搜索树：
  - 每个节点要么是红色，要么是黑色
  - 根节点是黑色
  - 每个叶节点（NIL节点，空节点）是黑色
  - 不能有相邻接的两个红色节点
  - 从任一节点到其每个叶子的所有路径都包含相同数目的黑色节点