# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid using fast and slow pointers, mid has to be the first middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None # split the list
        prev = None

        # reverse second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halves
        second = prev
        first = head

        while second: # use second since second is shorter 
        # 1 2  3 4 5
        # 1 5 
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            







        


