# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''DFS'''
        # def dfs(root, level):
        #     if not root: return level
        #     left = dfs(root.left, level+1)
        #     right = dfs(root.right, level+1)
        #     return max(left, right)
        # return dfs(root, 0)
        '''BFS'''
        if not root: return 0
        q = collections.deque([root])
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level += 1
        return level