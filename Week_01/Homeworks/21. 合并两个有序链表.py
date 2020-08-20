# https://leetcode-cn.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 指针操作：
        cur = dummy = ListNode(0)
        prev = None
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next, l1= l1, l1.next
                cur = cur.next
            else:
                cur.next, l2 = l2, l2.next
                cur = cur.next
        if l1: cur.next = l1
        if l2: cur.next = l2
        return dummy.next
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         # 递归法，O(n), O(n)，空间复杂度因为递归每次需要把中间值压栈
#         # merge(l1, l2) = merge(l1.next, l2) if l1.val < l2.val else merge(l1, l2.next)
#         # 终止条件
#         if not l1: 
#             return l2
#         if not l2:
#             return l1
        
#         if l1.val <= l2.val:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1, l2.next)
#             return l2        