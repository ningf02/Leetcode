# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next

        reverse_prev = None
        current = prev.next
        for _ in range(right-left+1):
            next_node = current.next
            current.next = reverse_prev
            reverse_prev = current
            current = next_node
        
        prev.next.next = current
        prev.next = reverse_prev
        return dummy.next
        
