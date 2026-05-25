# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse
        pre, cur = None, head

        if not cur.next:
            return pre

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        newHead = pre

        # remove
        if n == 1:
            newHead = newHead.next
        else:
            cur, pre = newHead, None
            for i in range(n-1):
                pre = cur
                cur = cur.next
            pre.next = cur.next


        # reverse
        pre, cur = None, newHead

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre




