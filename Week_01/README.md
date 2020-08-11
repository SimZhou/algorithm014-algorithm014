# 第一周学习笔记

## 学习方法

- 5分钟不会，直接看题解，理解后自己写出
- 查看其它思路
- 查看国际站最优思路
- 重复，过遍数

刻意练习，**记忆**+理解



## 刷题记录

本周做题

| #    | 题目名                                                       | 难度  | 关键词               | 已过遍数 |
| ---- | ------------------------------------------------------------ | ----- | -------------------- | -------- |
| 11   | [盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/) | 💛中等 | 数组，双指针         | 2        |
| 70   | [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)  | 💚简单 | DP                   | 2        |
| 15   | [三数之和](https://leetcode-cn.com/problems/3sum/)           | 💛中等 | 数组，双指针，哈希表 | 1        |
| 66   | [加一](https://leetcode-cn.com/problems/plus-one/)           | 💚简单 | 数组                 | 2        |

作业题

| #    | 题目名                                                       | 难度  | 关键词       | 已过遍数 |
| ---- | ------------------------------------------------------------ | ----- | ------------ | -------- |
|      | 改写 Deque (用add first/last)                                |       |              |          |
|      | 分析 Queue 和 Priority Queue                                 |       |              |          |
| 26   | [删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/) | 💚简单 | 数组，双指针 |          |
|      | [旋转数组](https://leetcode-cn.com/problems/rotate-array/)   | 💚简单 |              |          |
|      | [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) | 💚简单 |              |          |
|      | [合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/) | 💚简单 |              |          |
| 1    | [两数之和](https://leetcode-cn.com/problems/two-sum/)        | 💚简单 | 数组，哈希表 | 2        |
| 283  | [移动零](https://leetcode-cn.com/problems/move-zeroes/)      | 💚简单 | 数组，双指针 | 1        |
|      | [加一](https://leetcode-cn.com/problems/plus-one/)           | 💚简单 |              |          |
|      | [设计循环双端队列](https://leetcode.com/problems/design-circular-deque) | 💛中等 |              |          |
|      | [接雨水](https://leetcode.com/problems/trapping-rain-water/) | 🧡困难 |              |          |



## 视频笔记

### 1. 数组，链表，跳表

数组：在内存中开辟连续的内存地址，存储元素

链表：当前Node对象储存当前节点值与下一节点内存地址

跳表：带有跳表索引的链表，只能用于**元素有序**的情况下，用来取代平衡树二分查找

|          | 左append | 右append | 查询     | 插入     | 删除     |
| -------- | -------- | -------- | -------- | -------- | -------- |
| 数组     | O(1)     | O(1)     | O(1)     | O(n)     | O(n)     |
| 普通链表 | O(1)     | O(1)     | O(n)     | O(1)     | O(1)     |
| 跳表     | O(1)     | O(1)     | O(log n) | O(log n) | O(log n) |

空间复杂度上，数组最少，普通链表第二，跳表最高，但，都是O(n)。

链表应用：LRU Cache

跳表应用：Redis

### 2. 栈和队列

