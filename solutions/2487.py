# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        current = head
        while current:
            next_node = current.next
            current.next = rev
            rev = current
            current = next_node
        
        dummy = ListNode(rev.val)
        new = dummy
        num = rev.val
        while rev:            
            if rev.next and rev.next.val >= num:
                num = rev.next.val
                new.next = rev.next
                new = new.next
            rev = rev.next
        new.next = None
        
        rev2 = None
        current2 = dummy
        while current2:
            next_node = current2.next
            current2.next = rev2
            rev2 = current2
            current2 = next_node
        
        return rev2
