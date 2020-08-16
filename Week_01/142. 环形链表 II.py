# https://leetcode-cn.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        t, h  = head, head
        while 1: 
            if not h or not h.next: return
            t, h = t.next, h.next.next
            if t == h: break   
        while head != t:
            head, t = head.next, t.next
        return head