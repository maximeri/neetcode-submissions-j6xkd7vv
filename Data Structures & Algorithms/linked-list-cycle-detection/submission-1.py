# Hsuan Hsuan

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr1 = head
        curr2 = head.next

        while curr2 and curr2.next:
            if curr1.val == curr2.val:
                return True
            curr2 = curr2.next.next
            curr1 = curr1.next
        return False