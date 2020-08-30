# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == len(inorder) == 1: return TreeNode(preorder[0])
        if len(preorder) == len(inorder) == 0: return None
        
        root = TreeNode(preorder[0])
        rootindex = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+rootindex], inorder[0:rootindex])
        # 要特别注意这里的下标范围
        root.right = self.buildTree(preorder[rootindex+1:], inorder[rootindex+1:])
        return root