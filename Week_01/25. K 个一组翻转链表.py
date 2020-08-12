# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy, dummy.next = ListNode(0), head
        
        prev, cur = dummy, dummy.next
        
        while 1:
            ready = k
            guard = prev
            for _ in range(k):
                guard = guard.next
                if guard == None: 
                    ready = 0
                    break
            if not ready: break
                
            for _ in range(k-1):
                # prev.next, cur.next, cur.next.next = cur.next, cur.next.next, prev.next
                # cur.next.next, prev.next, cur.next = prev.next, cur.next, cur.next.next
                prev.next, cur.next.next, cur.next = cur.next, prev.next, cur.next.next
                
            prev, cur = cur, cur.next
        return dummy.next