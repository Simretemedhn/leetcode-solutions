# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head 
        size = 0 
        curr = head 
        while curr:
            size += 1 
            curr = curr.next 

        shift = k % size 
        if shift == 0:
            return head 

        # shifting the last shift amount of node to the begining 
        # starting from index size - k (the new head will be the one at the index of size - k, then connexting it to the begining )
        index = size - shift 
        curr = head 
        for _ in range(index-1):
            curr = curr.next 
        final_head = curr.next
        curr.next = None  

        curr = final_head 
        while curr.next:
            curr = curr.next 
        curr.next = head 
        return final_head 
    

