# https://leetcode-cn.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1, p2 = head, head
        while 1:
            if not p2 or not p2.next: return False
            p1, p2 = p1.next, p2.next.next
            if p1 == p2: return True