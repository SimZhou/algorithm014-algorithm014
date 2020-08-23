# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     res, stack, cur = [], [], root
    #     while stack or cur:
    #         while cur:
    #             stack.append(cur.right)
    #             cur = cur.right
    #         cur = stack.pop()
    #         res.append(cur.val)
    #         cur = cur.left
    # 递归
    def __init__(self):
        self.res = []
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.res.append(root.val)
        return self.res