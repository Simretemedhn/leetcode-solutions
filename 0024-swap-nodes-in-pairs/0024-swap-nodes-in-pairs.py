# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative approach 
        if not head or not head.next:
            return head
        
        # Dummy node to simplify handling
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            # Nodes to swap
            first = prev.next
            second = prev.next.next
            
            # Swapping
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move to next pair
            prev = first
        
        return dummy.next