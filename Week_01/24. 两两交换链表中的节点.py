# https://leetcode-cn.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy, dummy.next = ListNode(0), head
        
        prev, cur = dummy, dummy.next
        
        while 1:
            if not cur or not cur.next: break
            
            prev.next, cur.next.next, cur.next = cur.next, prev.next, cur.next.next
            
            prev = prev.next.next
            cur = prev.next
        
        return dummy.next