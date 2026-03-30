# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case
        if not lists or len(lists) == 0:
            return None
        
        
        return self.mergeSort(lists, 0, len(lists) - 1)

    def mergeSort(self, lists, s, e):
        if e - s + 1 <= 1:
            return lists[s]

        m = (s + e) // 2

        left  = self.mergeSort(lists, s, m)
        right = self.mergeSort(lists, m + 1, e)

        return self.merge(left, right)  

    def merge(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next

        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next

        return dummy.next
        





