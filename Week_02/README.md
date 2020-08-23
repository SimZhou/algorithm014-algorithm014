# 第二周学习笔记

## Code Interview 技巧（4步）

1. clarification，和面试官沟通清楚题目的意思
2. possible solutions --> optimal (time & space)，介绍可能的解法，以及时间空间复杂度
3. code，写代码
4. test cases，测试样例



## 刷题记录

额外刷题，来自LC日推题，群内每日一题，随性刷题等

| #    | 题目名                                                       | 难度  | 关键词                                                       | 已过遍数 |
| ---- | ------------------------------------------------------------ | ----- | ------------------------------------------------------------ | -------- |
| 1021 | [删除最外层的括号](https://leetcode-cn.com/problems/remove-outermost-parentheses/) | 💚简单 | [栈](https://leetcode-cn.com/tag/stack/)                     | 2        |
| 258  | [各位相加](https://leetcode-cn.com/problems/add-digits/)     | 💚简单 | [数学](https://leetcode-cn.com/tag/math/)                    | 1        |
| 104  | [二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/) | 💚简单 | [树](https://leetcode-cn.com/tag/tree/)，[DFS](https://leetcode-cn.com/tag/depth-first-search/) | 1        |
| 679  | [24 点游戏](https://leetcode-cn.com/problems/24-game/)       | 🧡困难 |                                                              |          |

实践题

| #    | 题目名                                                       | 难度  | 关键词                                                       | 已过遍数 |
| ---- | ------------------------------------------------------------ | ----- | ------------------------------------------------------------ | -------- |
|      | [最小的 k 个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/) | 💚简单 | [堆](https://leetcode-cn.com/tag/heap/)，[分治法](https://leetcode-cn.com/tag/divide-and-conquer/) |          |
|      | [滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/) (堆解法) | 🧡困难 | [堆](https://leetcode-cn.com/tag/heap/)，[Sliding Window](https://leetcode-cn.com/tag/sliding-window/) |          |
|      | [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/) | 💛中等 | [DFS](https://leetcode-cn.com/tag/depth-first-search/), [BFS](https://leetcode-cn.com/tag/breadth-first-search/), [并查集](https://leetcode-cn.com/tag/union-find/) |          |

作业题

| #     | 题目名                                                       | 难度     | 关键词                                                       | 已过遍数     |
| ----- | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | ------------ |
| -     | 写一个关于 HashMap 的小总结                                  | -        | 设计，队列                                                   | 见下文       |
| 242   | [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/description/) | 💚简单    | [排序](https://leetcode-cn.com/tag/sort/)，[哈希表](https://leetcode-cn.com/tag/hash-table/) | 2            |
| 1     | [两数之和](https://leetcode-cn.com/problems/two-sum/description/) | 💚简单    | 数组，哈希表                                                 | 6            |
| 589   | [N 叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/) | 💚简单    | [树](https://leetcode-cn.com/tag/tree/)                      | 1            |
| 590   | [N 叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/) | 💚简单    | [树](https://leetcode-cn.com/tag/tree/)                      | 1            |
| -     | [HeapSort](https://www.geeksforgeeks.org/heap-sort/)         | -        | 堆排序                                                       | -            |
| 49    | [字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/) | 💛中等    | [哈希表](https://leetcode-cn.com/tag/hash-table/)，[字符串](https://leetcode-cn.com/tag/string/) | 2            |
| 94    | [二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) | 💛中等    | [栈](https://leetcode-cn.com/tag/stack/)，[树](https://leetcode-cn.com/tag/tree/)，[哈希表](https://leetcode-cn.com/tag/hash-table/) | 1            |
| 589   | [二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/) | 💛中等    | [栈](https://leetcode-cn.com/tag/stack/)，[树](https://leetcode-cn.com/tag/tree/) | 1            |
| 145   | [二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/) | 🧡困难    | [栈](https://leetcode-cn.com/tag/stack/)，[树](https://leetcode-cn.com/tag/tree/)，[哈希表](https://leetcode-cn.com/tag/hash-table/) | 1            |
| 429   | [N 叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/) | 💛中等    | [树](https://leetcode-cn.com/tag/tree/)，BFS                 | 1            |
| 264   | [丑数 II](https://leetcode-cn.com/problems/ugly-number-ii/)  | 💛中等    |                                                              |              |
| 347   | [前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/) | 💛中等    | 堆，哈希表                                                   | 1            |
| **#** | **预习**                                                     | **难度** | **关键词**                                                   | **已过遍数** |
| 22    | [括号生成](https://leetcode-cn.com/problems/generate-parentheses/) | 💛中等    | [字符串](https://leetcode-cn.com/tag/string/)，[回溯算法](https://leetcode-cn.com/tag/backtracking/) |              |
|       | [Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)        |          |                                                              |              |
|       | [子集](https://leetcode-cn.com/problems/subsets/)            |          |                                                              |              |
|       | [N 皇后](https://leetcode-cn.com/problems/n-queens/)         |          |                                                              |              |



## 视频笔记

### 1. 哈希表，映射，集合（实现与特性）

**哈希表**：也叫散列表，根据关键码值直接进行访问的数据结构。通过把关键码值映射到表中一个位置来访问记录。这个映射函数叫散列函数（Hash Function），存放记录的数组叫做哈希表（散列表）。

具体来讲，**hash(key) = value在内存中的地址**，直接访问该地址即可得到value。

※ 哈希碰撞：当不同key得到的hash值相同时，同一个内存地址对应多个value，就产生了哈希碰撞。

※ 哈希碰撞的解决方法：拉链式解决冲突法，将value在内存中储存的值改成一个链表，第一个值存在链表第1级，第二个碰撞的值存在链表第2级。

哈希表的**查找/插入/删除**时间复杂度皆为**O(1)**

###  2. 树，二叉树，二叉搜索树

> 加速数据结构的关键在于升维（比如链表->跳表）

**树**：就相当于是一个二维的链表，每个节点除了自己，都指向另外的两个元素。

※ 树和图的区别：如果有环，按照定义就不称为树，但可以是图。

※ 可以说，链表是特殊的树，树是特殊的图。

**二叉树**：每个节点有至多2个分叉的树。

> **满二叉树（Full Binary Tree）**：A binary tree T is full if each node is either a leaf or possesses exactly two child nodes.
>
> **完全二叉树（Complete Binary Tree）**：A binary tree T with n levels is complete if all levels except possibly the last are completely full,and the last level has all its nodes to the left side. 深度为K的完全二叉树，每个叶节点的深度只能为K或K-1，且要么只缺失右孩子或者左右孩子都缺失
>
> （把一颗二叉树按照从上到下，从左到右的顺序构建，就是一个完全二叉树）
>
> **完美二叉树（Perfect Binary Tree）**：A binary tree with all leaf nodes at the same depth. All internal nodes have degree 2.

**二叉搜索树**：又叫**二叉排序树**、**二叉查找树**、**有序二叉树**（Ordered Binary Tree）、**排序二叉树**（Sorted Binary Tree），是指一颗空树或者具有下列性质的二叉树：

1. 左子树上所有节点的值均小于它的根节点的值；
2. 右子树上所有节点的值均大于它的根节点的值；
3. 以此类推：左右子树也分别是二叉搜索树

※ 二叉搜索树特性：*中序遍历为升序排列*；访问、查找、插入、删除都是 $O(\log{n})$ 的复杂度

※ 二叉搜索树Demo：https://visualgo.net/zh/bst

> **其它树结构**：
>
> **AVL树（平衡二叉树）**：最先发明的自平衡的**二叉搜索树**。
>
> **红黑树**：许多“平衡“搜索树中的一种， 可以保证在最坏情况下基本动态集合操作的时间复杂度为O(lgN)。
>
> **B树**：B树与红黑树的不同之处在于B 树的结点可以有很多孩子，从数个到数于个。
>
> **B+树**：一个常见的B树变种，它把所有的卫星数据都存储在叶结点中，内部结点只存放关键字和孩子指针，因此最大化了内部结点的分支因子。
>
> **B\*树**：B+树一种变形，它是在B+树的基础上，将索引层以指针连接起来，使搜索取值更加快捷。

#### 二叉树的遍历

1. 前序（Pre-order）：根-左-右
2. 中序（In-order）：左-根-右
3. 后序（Post-order）：左-右-根

（区别在于根的位置）

```python
# 前序遍历
def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
# 中序遍历
def inorder(self, root):
    if root:
        self.preorder(root.left)
        self.traverse_path.append(root.val)
        self.preorder(root.right)
# 后序遍历
def postorder(self, root):
    if root:
        self.preorder(root.left)
        self.preorder(root.right)
        self.traverse_path.append(root.val)
```

### 3. 堆，二叉堆

**堆（Heap）**：可以迅速找到一堆数中最大或者最小值的数据结构。([Wikepedia: Heap](https://en.wikipedia.org/wiki/Heap_(data_structure)))

根节点最大的堆叫做大顶堆，根节点最小的堆叫做小顶堆。常见的堆有二叉堆，斐波那契堆等。

（大顶）堆的常见API有：

- find-max: O(1)
- delete-max: O(logN)
- insert (create): O(logN) or O(1)

※ 二叉堆性质：1. 是一颗**完全树**。2. 树中任意系节点值总是 >= 其子节点的值。

> 二叉堆**左右子节点索引计算方法**：
>
> - **根节点**（顶堆元素）是：a[0]
> - 对于任意一个节点 i，它的：
>   - **左子节点**索引为 **2i+1**
>   - **右子节点**索引为 **2i+2**
> - 索引为 i 的**父节点**索引是 **floor((i-1)/2)**

#### 堆的插入和删除

**插入元素 O(logN)**：将新元素放进最后一个空位的叶子节点，然后和它的父节点进行比较，如果大于/小于父节点，则将它与父节点进行交换。继续进行该操作直到不满足条件。（Sift Up）

**删除堆顶元素 O(logN)**：删除堆顶元素后，将堆尾元素替换到顶部，然后以此从根部下调整个堆的结构。（注意，若同时小于左右儿子，则需要和左右儿子中更大的一个进行交换）（Sift Down）

代码：[堆的实现](https://shimo.im/docs/Lw86vJzOGOMpWZz2/read)

### 4. 图

**图**：Graph(V, E)。顶点的属性：度（入度/出度）；边的属性：有向/无向、权重。

※ 图的表示：邻接矩阵；邻接表。

图的**DFS**递归：

```python
visited = set()

def dfs(node, visited):
    # Terminator
    if node in visited: 
        # already visited
        return
   	visited.add(node)
    
    # Process current node
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
```

图的**BFS**递归：

```python
def bfs(graph, start, end):
    
    queue = []				# 借助队列来实现BFS递归
    queue.append([start])	# 初始情况，把start节点加入队列
    
    visited = set()			
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
```

*注意*：图在dfs/bfs遍历时，一定要存visited矩阵（因为不像树，图可能存在环路）

**图的高级算法**：

1. 连通图个数：[200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)

2. 拓扑排序：[拓扑排序的实现方法以及环路检测](https://zhuanlan.zhihu.com/p/34871092)，[207. 课程表](https://leetcode-cn.com/problems/course-schedule/)
3. 最短路径：[Dijkstra](https://www.bilibili.com/video/av25829980?from=search&seid=13391343514095937158)
4. 最小生成树：[Minimum Spanning Tree](https://www.bilibili.com/video/av84820276?from=search&seid=17476598104352152051)



### 2020.08.20 超哥直播总结——面试考点

![面试考点](https://github.com/SimZhou/algorithm014-algorithm014/blob/master/Week_02/%E9%9D%A2%E8%AF%95%E8%80%83%E7%82%B9.png?raw=true)

#### 面试考点：

1. **项目经验**

   你在其中做了什么

   你产生了什么**影响力**（结果/收益）（为了通过HR简历筛选）

   突出**亮点**

2. **基础知识**

   根据岗位和所学专业会有所不同，Java开发会问Java基础，并发等；机器学习会问机器学习基础。这方面可以看一下面经。三个不错的资料：[CS-Notes](https://github.com/CyC2018/CS-Notes) (强推)，[JavaGuide](https://github.com/Snailclimb/JavaGuide)，[40 个 Java 多线程问题总结](https://juejin.im/entry/6844903474195333128)

3. **💎 算法与数据结构（重点） 60~70%**

   算法与数据结构更像*健身/学滑雪/学游泳*。方法有3个：

   - 脑图总结整体知识点，方便记忆。然后去深入学习每一块知识。+ 费曼学习法

     （Elon Musk：先学习主干知识，然后再深入细枝末节）

     （*题外话*：大公司的代码一般都是没有文档的，先找老人把代码大框架给你讲一遍，画成脑图，然后自己深入去看）

   - 动手练习（五毒神掌，艾宾浩斯记忆法）

   **误区**：[花一晚上也无法理解非递归遍历二叉树，我该继续学下去吗？ - 飞鼠明天做窝的回答 - 知乎](https://www.zhihu.com/question/387295413/answer/1154369980)

   - 光看不练
   - 只练一遍
   - 没有反馈

4. **系统设计（少量）**

   资料：[system-design-primer 系统设计入门](https://github.com/donnemartin/system-design-primer)

   

#### 正确认识面试：

- 作为和未来同事的一次合作（不要当成考试）
- 并肩作战，解决问题
- 减少压力

**※ 一定要积极地沟通和表达，建立同理心**



#### QA：

关于落差：刷题学到的东西在工作中只能用到1%，怎么办？

关键是学到学习方法，使用**正确的学习方法**来学习业务的东西，并且基础扎实了，能够让自己更好地专注业务内容。

