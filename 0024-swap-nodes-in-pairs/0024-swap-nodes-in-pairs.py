# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        
        front = head.next
        head.next = self.swapPairs(head.next.next)
        front.next = head
        
        return front