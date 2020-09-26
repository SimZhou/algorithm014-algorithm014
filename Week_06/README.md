# 第6周学习笔记

本周学习：

- 动态规划



## 刷题记录

额外刷题，来自LC日推题，群内每日一题，随性刷题等

| #    | 题目名                                                      | 难度  | 关键词                                                 | 已过遍数 |
| ---- | ----------------------------------------------------------- | ----- | ------------------------------------------------------ | -------- |
| 474  | [一和零](https://leetcode-cn.com/problems/ones-and-zeroes/) | 💛中等 | [DP](https://leetcode-cn.com/tag/dynamic-programming/) |          |
|      | [目标和](https://leetcode-cn.com/problems/target-sum/)      | 💛中等 | [DP](https://leetcode-cn.com/tag/dynamic-programming/) |          |
|      |                                                             | 💚简单 |                                                        |          |
| 456  | [132模式](https://leetcode-cn.com/problems/132-pattern/)    | 💛中等 | [DP](https://leetcode-cn.com/tag/dynamic-programming/) |          |

实践题

| #    | 题目名                                                       | 难度  | 关键词                                                       | 已过遍数 |
| ---- | ------------------------------------------------------------ | ----- | ------------------------------------------------------------ | -------- |
| 62   | [不同路径](https://leetcode-cn.com/problems/unique-paths/)   | 💛中等 | 数组，[DP](https://leetcode-cn.com/tag/dynamic-programming/) | 1        |
| 63   | [不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/) | 💛中等 | 数组，[DP](https://leetcode-cn.com/tag/dynamic-programming/) | 1        |
| 980  | [不同路径 III](https://leetcode-cn.com/problems/unique-paths-iii/) | 🧡困难 | DFS，回溯                                                    |          |
| 1143 | [最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/) | 💛中等 | DP                                                           | 2        |
| ※    | [MIT 动态规划课程最短路径算法](https://www.bilibili.com/video/av53233912?from=search&seid=2847395688604491997) | 💙视频 | 学习视频                                                     | -        |
|      | [三角形最小路径和](https://leetcode-cn.com/problems/triangle/description/) |       |                                                              |          |
| ※    | [三角形最小路径和高票回答](https://leetcode.com/problems/triangle/discuss/38735/Python-easy-to-understand-solutions-(top-down-bottom-up)) | 💙题解 | 学习题解                                                     | -        |
|      | [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/) |       |                                                              |          |
| 152  | [乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray/description/) | 💛中等 | 数组，[DP](https://leetcode-cn.com/tag/dynamic-programming/) | 1        |
|      | [零钱兑换](https://leetcode-cn.com/problems/coin-change/description/) |       |                                                              |          |
|      | [零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2/) |       |                                                              |          |
|      | [完全平方数](https://leetcode-cn.com/problems/perfect-squares/) |       |                                                              |          |

作业题

| #    | 题目名                                                       | 难度  | 关键词                                                 | 已过遍数 |
| ---- | ------------------------------------------------------------ | ----- | ------------------------------------------------------ | -------- |
| 64   | [最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/) | 💛中等 | [DP](https://leetcode-cn.com/tag/dynamic-programming/) |          |
|      | [解码方法](https://leetcode-cn.com/problems/decode-ways)     | 💛中等 |                                                        |          |
|      | [最大正方形](https://leetcode-cn.com/problems/maximal-square/) | 💛中等 |                                                        |          |
|      | [任务调度器](https://leetcode-cn.com/problems/task-scheduler/) | 💛中等 |                                                        |          |
|      | [回文子串](https://leetcode-cn.com/problems/palindromic-substrings/) | 💛中等 |                                                        |          |
|      | [最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/) | 🧡困难 |                                                        |          |
| 72   | *[编辑距离](https://leetcode-cn.com/problems/edit-distance/) | 🧡困难 | DP                                                     | 3        |
|      | [矩形区域不超过 K 的最大数值和](https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/) | 🧡困难 |                                                        |          |
|      | [青蛙过河](https://leetcode-cn.com/problems/frog-jump/)      | 🧡困难 |                                                        |          |
|      | [分割数组的最大值](https://leetcode-cn.com/problems/split-array-largest-sum) | 🧡困难 |                                                        |          |
|      | [学生出勤记录 II](https://leetcode-cn.com/problems/student-attendance-record-ii/) | 🧡困难 |                                                        |          |
|      | [最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/) | 🧡困难 |                                                        |          |
|      | [戳气球](https://leetcode-cn.com/problems/burst-balloons/)   | 🧡困难 |                                                        |          |



## 视频笔记

### 1. 动态规划

- DP和递归或者分治 没有本质上的区别（关键看有无最优子结构）
- 共性：找到重复子问题
- 差异性：动态规划有最优子结构、中途可以淘汰次优解

[MIT动态规划视频](https://www.bilibili.com/video/av53233912?from=search&seid=2847395688604491997)提到的5步DP法：

1. 定义子问题
2. 猜（部分解）
3. 合并子问题的解
4. 递归+记忆（自顶向下） or 建立DP表（自底向上）
5. 解决原问题



## 2020.09.17 直播分享 - 如何在职场中发挥自己的价值

- 推荐书：《潜规则》—— 吴思
- 同理心 - 站在对方的角度看问题
- 正确认识公司：（讲了Facebook的PC端流量走向移动端时的广告投放问题的故事）不要看公司的各种东西都看不顺眼，要看到问题背后的机遇。公司有1个成功的产品，背后就一定有9个失败的产品。
- 你对你们team的贡献是什么？你对你们公司的核心价值是什么？
- 元认知：跳出自己和他人的情绪，站在上帝视角理性地看待自己和他人关系的认知能力
- 简单的工作有着一种诱惑力，诱惑者那些没有定力的人去做，一直做……（ToDoList要做成一个优先队列，优先处理那些更有价值的事情）
- 人是一个对象，有一套自己的API（人性），要懂得人性和顺应人性
- 不要相信人，要相信人性
- 推荐书：《优势识别器 2.0》
- 具体步骤：
  - 1~3年的新人：成为某一块业务的专家（authority）（10000小时定律）
  - 2~4年进阶：努力，进阶，压力大，请求资源（人力，钱），然后走向管理；只管耕耘，不问收获（肯尼迪演讲）

QA：

1. 元认知举例：别人对你有情绪一般来讲都不是针对你个人，比如说客户打客服热线大骂客服发脾气，一般来讲肯定是因为产品不好，而不是针对客服本人。