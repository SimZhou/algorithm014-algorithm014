# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''BFS'''
        if not root: return []
        q, res = deque([root]), []
        while q:
            restemp = []
            for i in range(len(q)):
                node = q.popleft()
                restemp.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(restemp)
        return res