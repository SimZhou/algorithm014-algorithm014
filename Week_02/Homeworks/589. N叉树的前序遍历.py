# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/

class Solution:
    # 借助栈，实现DFS
    def preorder(self, root: 'Node') -> List[int]:
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node: 
                res.append(node.val)
                [stack.append(child) for child in node.children[::-1]];
        return res
        
    # # 递归
    # def __init__(self):
    #     self.res = []
    # def preorder(self, root: 'Node') -> List[int]:
    #     if root:
    #         self.res.append(root.val)
    #         for node in root.children:
    #             self.preorder(node)
    #     return self.res