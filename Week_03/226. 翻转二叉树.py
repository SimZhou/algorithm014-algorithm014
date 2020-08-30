# https://leetcode-cn.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # # 迭代法，用队列（BFS）
        # queue = [root]
        # while queue:
        #     node = queue.pop(0)
        #     if node: 
        #         node.left, node.right = node.right, node.left
        #         queue.append(node.left)
        #         queue.append(node.right)
        # return root
    
        # 迭代法，用栈（DFS）
        queue = [root]
        while queue:
            node = queue.pop()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
        
        # # 对每一个node，如果它不为空，执行如下操作：
        # # node.left, node.right = node.right, node.left
        # if not root: return
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root