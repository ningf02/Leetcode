# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while head:
            if head.val != val:
                current.next = head
                current = current.next
            head = head.next
        current.next = None
        return dummy.next
        
