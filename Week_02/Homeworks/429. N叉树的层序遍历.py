# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        stack, res = [root], []
        while stack:
            r = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                r.append(node.val)
                [stack.append(child) for child in node.children];
            res.append(r)
        return res