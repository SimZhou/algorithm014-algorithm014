# https://leetcode-cn.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        # Python语法糖写法
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev

    # def reverseList(self, head: ListNode) -> ListNode:
    #     prev = None
    #     while head:
    #         pro = head.next
    #         head.next = prev
    #         prev = head
    #         head = pro