# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)
        current = dummy
        while head:
            if head.val != current.val:
                current.next = head
                current = current.next
            head = head.next
        current.next = None
        return dummy.next
        
        
