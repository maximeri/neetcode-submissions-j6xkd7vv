# Hsuan Hsuan

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        curr1 = list1
        curr2 = list2
        curr = dummy
        while curr1 or curr2:
            if not curr2:
                curr.next = curr1
                curr1 = curr1.next
            elif not curr1:
                curr.next = curr2
                curr2 = curr2.next
            elif curr1.val > curr2.val:
                curr.next = curr2
                curr2 = curr2.next
            else:
                curr.next = curr1
                curr1 = curr1.next
            curr = curr.next
        
        return dummy.next
