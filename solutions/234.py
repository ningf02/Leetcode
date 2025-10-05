# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        current = head
        while current:
            new_node = ListNode(current.val)
            new_node.next = rev
            rev = new_node
            current = current.next
        
        while rev and head:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        
        return True


        
        
