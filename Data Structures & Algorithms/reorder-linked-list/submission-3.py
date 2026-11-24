# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 24 6810 split
        # 24 1086 cut and reverse 2nd half
        # 210486 glue

        # 2 4 6
        # 4 6

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        cur = slow.next
        slow.next = None # cut
        pre = None

        while cur:
            newCur = cur.next
            cur.next = pre
            pre = cur
            cur = newCur

        dummy = ListNode(0)
        cur, half1, half2, = dummy, head, pre

        while half1:
            cur.next = half1
            cur = cur.next
            half1 = half1.next

            if half2:
                cur.next = half2
                cur = cur.next
                half2 = half2.next








        


