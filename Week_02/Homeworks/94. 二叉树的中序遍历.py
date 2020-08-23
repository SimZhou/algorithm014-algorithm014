# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 借助栈来实现
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [], []
        cur = root
        while cur or stack:
            while cur:             # 只要当前节点有左孩子
                stack.append(cur)  # 都会优先处理左孩子
                cur = cur.left
            cur = stack.pop()      # 取出
            res.append(cur.val)    # 
            cur = cur.right       # 如果有右孩子，这时会把右孩子放进去
            # print(stack)
            
        return res
    
    # # 递归
    # def __init__(self):
    #     self.res = []
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if root:
    #         self.inorderTraversal(root.left)
    #         self.res.append(root.val)
    #         self.inorderTraversal(root.right)
    #     return self.res