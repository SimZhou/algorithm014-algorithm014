# https://leetcode-cn.com/problems/reverse-linked-list-ii/

class Solution:
    def reverseBetween(self, head, m, n):
        dummy, dummy.next = ListNode(0), head
        cur, prev = head, dummy
        for _ in range(m - 1):
            cur, prev = cur.next, prev.next
        for _ in range(n - m):
            cur.next.next, prev.next, cur.next = prev.next, cur.next, cur.next.next
        return dummy.next