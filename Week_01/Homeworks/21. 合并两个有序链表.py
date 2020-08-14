# https://leetcode-cn.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 递归法，O(n), O(n)，空间复杂度因为递归每次需要把中间值压栈
        # merge(l1, l2) = merge(l1.next, l2) if l1.val < l2.val else merge(l1, l2.next)
        # 终止条件
        if not l1:
            return l2
        if not l2: 
            return l1
        
        dum = ListNode(None)
        if l1.val < l2.val:
            dum.next = l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        else:
            dum.next = l2
            l2.next = self.mergeTwoLists(l1, l2.next)
        return dum.next
        
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     # 指针操作法；
    #     # 复杂度：O(n), O(1)
    #     dummy = ListNode(None)
    #     prev = dummy
    #     while l1 and l2:
    #         if l1.val <= l2.val: 
    #             prev.next = l1
    #             l1, prev = l1.next, prev.next
    #         else: 
    #             prev.next = l2
    #             l2, prev = l2.next, prev.next
    #     if not l1: prev.next = l2
    #     if not l2: prev.next = l1
    #     return dummy.next