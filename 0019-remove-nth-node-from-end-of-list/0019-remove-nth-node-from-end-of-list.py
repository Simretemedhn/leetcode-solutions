# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        size = 0
        current = head
        while current:
            size += 1
            current = current.next
        
        remove_index = size - n
        
        current = dummy
        for _ in range(remove_index):
            current = current.next
        
        current.next = current.next.next
        
        return dummy.next

