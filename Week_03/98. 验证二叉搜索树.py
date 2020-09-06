# https://leetcode-cn.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
    #     '''递归'''
    #     lb, rb = float("-inf"), float("inf")
    #     def dfs(root, lb, rb):
    #         if not root: return True
    #         left = dfs(root.left, lb, root.val)
    #         right = dfs(root.right, root.val, rb)
    #         # 当前节点是否有效，取决于左右子树是否有效，以及当前节点是否有效
    #         if left and right and lb < root.val < rb: return True
    #         else: return False
    #     return dfs(root, lb, rb)
    
        '''中序遍历'''
        pre = float("-inf")
        def inorder(root):
            nonlocal pre
            if not root: return True
            if not inorder(root.left): return False
            if root.val <= pre: return False
            pre = root.val
            return inorder(root.right)
        return inorder(root)