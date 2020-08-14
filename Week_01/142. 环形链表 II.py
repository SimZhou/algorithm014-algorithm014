# https://leetcode-cn.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        tortoise, hare = head, head
        while 1:
            if not hare: return
            if not hare.next: return
            
            tortoise = tortoise.next
            hare = hare.next.next
            
            if tortoise == hare: break
            
        while head != tortoise:
            head = head.next
            tortoise = tortoise.next
        
        return head