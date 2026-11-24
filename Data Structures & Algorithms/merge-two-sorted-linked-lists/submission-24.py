# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur, curL1, curL2 = dummy, list1, list2

        while curL1 and curL2:
            if curL1.val <= curL2.val:
                cur.next = curL1
                curL1 = curL1.next
            else:
                cur.next = curL2
                curL2 = curL2.next
            cur = cur.next

        if curL1:
            cur.next = curL1
        elif curL2:
            cur.next = curL2

        return dummy.next





