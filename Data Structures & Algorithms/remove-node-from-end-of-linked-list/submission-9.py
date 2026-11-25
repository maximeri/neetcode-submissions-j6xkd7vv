# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head

        while cur:
            length += 1
            cur = cur.next

        dummy = ListNode(0, head)
        cur = dummy
        order = length - n

        while order > 0:
            cur = cur.next
            order -= 1

        target = cur.next
        newNxt = None

        if target:
            newNxt = target.next

        cur.next = newNxt
        target.next = None

        return dummy.next




        
