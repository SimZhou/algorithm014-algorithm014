# 第3周学习笔记

[写在20年初的校招面试心得与自学CS经验及找工作分享](https://github.com/conanhujinming/tips_for_interview/blob/master/README-zh_CN.md)

[线段树入门](https://mp.weixin.qq.com/s?__biz=MzU2OTUyNzk1NQ==&mid=2247490915&idx=1&sn=a5db58060b20a9192607e2c5a7aac1ac&source=41#wechat_redirect)

本周学习：

- 递归
- 分治
- 回溯

## 刷题记录

额外刷题，来自LC日推题，群内每日一题，随性刷题等

| #    | 题目名                                                       | 难度  | 关键词                                        | 已过遍数 |
| ---- | ------------------------------------------------------------ | ----- | --------------------------------------------- | -------- |
| 313  | [超级丑数](https://leetcode-cn.com/problems/super-ugly-number/) | 💛中等 | [堆](https://leetcode-cn.com/tag/heap/)，数学 |          |
| 679  | [24 点游戏](https://leetcode-cn.com/problems/24-game/)       | 🧡困难 |                                               |          |
| 5    | *[最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/) | 💛中等 | 字符串，DP                                    | 1        |
| -    | [面试题 17.09. 第 k 个数](https://leetcode-cn.com/problems/get-kth-magic-number-lcci/) | 💛中等 | 丑数                                          | 1        |

实践题

| #    | 题目名                                                       | 难度  | 关键词                                                       | 已过遍数 |
| ---- | ------------------------------------------------------------ | ----- | ------------------------------------------------------------ | -------- |
| 22   | [括号生成](https://leetcode-cn.com/problems/generate-parentheses/) | 💛中等 | [字符串](https://leetcode-cn.com/tag/string/)，[回溯算法](https://leetcode-cn.com/tag/backtracking/) | 2        |
| 70   | [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)  | 💚简单 | 动态规划                                                     | 老生常谈 |
| 226  | [翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/description/) | 💚简单 | 树                                                           | 1        |
| 98   | [验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree) | 💛中等 | 数，DFS                                                      | 1        |
| 104  | [二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree) | 💚简单 | 树，DFS                                                      | 1        |
| 111  | [二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree) | 💚简单 | 树，DFS                                                      | 1        |
| 297  | [二叉树的序列化与反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/) | 🧡困难 | 树，设计                                                     |          |
| 50   | [Pow(x, n) ](https://leetcode-cn.com/problems/powx-n/)       | 💛中等 | 数学，二分查找                                               | 1        |
| 78   | [子集](https://leetcode-cn.com/problems/subsets/)            | 💛中等 | 位运算，数组，回溯                                           | 1        |
| 17   | [电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/) | 💛中等 | [字符串](https://leetcode-cn.com/tag/string/)，[回溯算法](https://leetcode-cn.com/tag/backtracking/) | 2        |
| 169  | [多数元素](https://leetcode-cn.com/problems/majority-element/description/) | 💚简单 | 位运算，数组，分治                                           | 1        |
| 51   | [N 皇后](https://leetcode-cn.com/problems/n-queens/)         | 🧡困难 | 回溯                                                         | 1        |

作业题

| #    | 题目名                                                       | 难度  | 关键词        | 已过遍数 |
| ---- | ------------------------------------------------------------ | ----- | ------------- | -------- |
| 236  | [二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/) | 💛中等 | 树            | 2        |
| 105  | [从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | 💛中等 | 树，DFS，数组 | 1        |
| 77   | [组合](https://leetcode-cn.com/problems/combinations/)       | 💛中等 | 回溯算法      | 0.5      |
| 46   | [全排列](https://leetcode-cn.com/problems/permutations/)     | 💛中等 | 回溯算法      | 1        |
| 47   | [全排列 II](https://leetcode-cn.com/problems/permutations-ii/) | 💛中等 | 回溯算法      | 1        |



## 视频笔记

### 1. 递归

递归≈循环，只不过是通过函数体调用自己进行。它们在执行时没有明显的边界。

递归属性：1. 向下进入递归，向上返回递归。2. 通过return返回上一层。3. 每一层的环境和变量都是一份拷贝

例子：阶乘：factorial(n) = factorial(n-1) * n (if n = 1, return 1)

```python
factorial(6)
6 * factorial(5)
6 * (5 * factorial(4))
6 * (5 * (4 * factorial(3)))
6 * (5 * (4 * (3 * factorial(2))))
6 * (5 * (4 * (3 * (2 * factorial(1)))))
6 * (5 * (4 * (3 * (2 * 1))))
6 * (5 * (4 * (3 * 2)))
6 * (5 * (4 * 6))
6 * (5 * 24)
6 * 120
720
```

递归模板：

```python
def recursion(level, param1, param2, ...):
    # Terminator
    if level > MAX_LEVEL:
        process_result
        return				# 终止条件
    
    # Process logic in current level
    process(level, data...)
    # drill down
    self.recursion(level+1, p1, ...)
    # reverse the current level status if needed(回溯，清理全局变量)
    ...
```

### 2. 分治、回溯

分治，回溯本质上都是递归。

分治与普通递归最大的不同是，有一个把子问题合并的过程。

分治模板：

```python
def divide_conquer(problem, param1, param2, ...):
    # Recursion terminator
    if problem is None:
        print_result
        return
    # Prepare data
    data = prepare_data(problem)
   	subproblems = split_problem(problem, data)
    # Conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)
    ...
    # process and generate the final result
    result = process_result(subresult1, subresult2, ...)
```

回溯在深入到树底部但未找到正确答案时，会回退中间的查找结果，然后到别的分叉查找答案。



### 2020.08.27直播：题以类聚—手把手带你搞定大厂算法面试题

#### 专题一：递归

46 全排列

22 括号生成

17 电话号码生成

八皇后

N皇后

101 对称二叉树

