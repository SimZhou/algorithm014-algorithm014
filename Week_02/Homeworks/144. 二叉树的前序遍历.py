# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 借助栈来实现
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node: 
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
    
    # # 递归
    # def __init__(self):
    #     self.res = []
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     if root:
    #         self.res.append(root.val)
    #         self.preorderTraversal(root.left)
    #         self.preorderTraversal(root.right)
    #     return self.res