# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        right = slow.next
        slow.next = None

        # reverse right half
        prev, cur = None, right
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        right = prev

        left = head

        while left and right:
            l_nxt, r_nxt = left.next, right.next
            left.next = right
            right.next = l_nxt
            left, right = l_nxt, r_nxt




