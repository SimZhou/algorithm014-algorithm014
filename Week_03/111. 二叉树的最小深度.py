# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''DFS'''
        # def dfs(root, level):
        #     if not root: return level
        #     if not root.left and not root.right: return level+1
        #     left = dfs(root.left, level+1)
        #     right = dfs(root.right, level+1)
        #     if not root.left: return right
        #     if not root.right: return left
        #     return min(left, right)  
        # return dfs(root, 0)
        
        '''BFS'''
        if not root: return 0
        q = collections.deque([root])
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right: return level + 1
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level += 1