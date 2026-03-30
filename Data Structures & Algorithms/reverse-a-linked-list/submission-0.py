# Hsuan Hsuan

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # rescursion
        # you enter the recursion first then you come back
        # remember to clean the .next node along the way
        # how to return the new head
        # the recurrsion return value is used to return the new head
        # during the recurrsion process you can just revert the node along the way
        # no need to rely on the return value

        # iteration
        if not head:
            return
        
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev

