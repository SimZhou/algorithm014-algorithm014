# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    # 递归
    def __init__(self):
        self.res = []
    def postorder(self, root: 'Node') -> List[int]:
        if root:
            [self.postorder(node) for node in root.children[::]];
            self.res.append(root.val)
        return self.res