# https://leetcode-cn.com/problems/trapping-rain-water/

# 双指针：找所有起始和终止，
# 什么作为起始？height[i+1] < height[i] 的，都可以作为起始。
# 终止：height[x] >= height[i]，则x为终止
# 时间：O(n)，空间：O(1)
# × ！不可行！

# 暴力法：
# 对于每一根柱子，找到它往右可能的右边界，
# × 貌似不可行

# 暴力法1：
# 对于每一个点，找到它往左右延申的最大高度，来确定这个点上面可以堆积多少水
# 具体来讲，左边A = max(a)，右边B = max(b)，水(x) = min(A, B) - x 
#（木桶原理）
# 复杂度O(n^2),O(1)

# 暴力法2：从上到下把水往下倒（一层一层计算）
# 时间：O(kn)，k为最大高度，空间：O(1)

# 单调栈：递减的入栈，递增的开始出栈并计算
# 时间：O(n)，空间：O(n)

# 动态编程：同暴力法1，但是因为对于每个i，都有一个max_left和一个max_right，所以只需要提前储存好两个max表即可
# 具体来讲，存A[i] = max(a)[i], B[i] = max(b)[i]，Water(i) = min(A[i], B[i]) - height[i]

class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        动态编程
        '''
        if len(height) <= 1: return 0
        A, B = [height[0]], [height[-1]]
        for i in range(1, len(height)):
            A.append(max(A[-1], height[i]))
        for i in range(len(height)-2, -1, -1):
            B = [max(B[0], height[i])] + B
        res = 0
        for i in range(len(height)):
            res += min(A[i], B[i]) - height[i] >= 0 and min(A[i], B[i]) - height[i] or 0
        return res
        
        # '''
        # 单调栈 —— 单调递减栈，如果碰到增的，就可以开始计算左边的对应Trap了。trap也是分层计算。计算完即可出栈。
        # '''
        # stack = []
        # res = 0
        # for i in range(len(height)):
        #     while stack and stack[-1][1] <= height[i]:
        #         cur_i, cur_height = stack.pop()
        #         if not stack: break
        #         _h = min(stack[-1][1], height[i]) - cur_height
        #         cur_width = i - stack[-1][0] - 1
        #         res += cur_width * _h
        #         # print(stack, cur_width * _h)
        #     # 只要stack为空 或者 栈顶元素大于新加元素，则继续添加
        #     stack.append((i, height[i]))
        #     # print(stack)
        # return res
    
#         '''
#         一层一层算，可以不先找最大层数k，只需要遍历到层Trap为0即可。No不可，第一层可能没有的
#         超时了
#         '''
#         if not height: return 0
        
#         def layerTrap(h: List[int]) -> int:
#             # 输入一个列表，找到当前层可以积水多少。输入列表为消层后的列表，可以有大于1的数。
#             # 栈解
#             stack, layerRes = [], 0
#             for i in range(len(h)):
#                 if h[i]: 
#                     if stack: layerRes += i - stack.pop(0) - 1
#                     stack.append(i)
#             return layerRes
        
#         k = max(height)
#         res = 0
#         for i in range(k):
#             layerRes = layerTrap(height)
#             res += layerRes
#             height = list(map(lambda x: x-1>=0 and x-1 or 0, height))
#             # print(layerRes)
#         return res

        
        # '''
        # 暴力法2，木桶原理 On**2 O1 —— 超时
        # '''
        # water = 0
        # for i in range(1, len(height)-1):
        #     leftmax = 0
        #     rightmax = 0
        #     for _ in range(0, i):
        #         leftmax = max(leftmax, height[_])
        #     for _ in range(i+1, len(height)):
        #         rightmax = max(rightmax, height[_])
        #     water += max(min(leftmax, rightmax) - height[i], 0)
        # return water