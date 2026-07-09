# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:  
            return head
        
        curr = head 
        dummy = ListNode(0)
        last = dummy 

        while curr:
            is_dup = False 
            while curr.next and curr.next.val == curr.val:
                is_dup = True 
                curr = curr.next 
            
            if not is_dup:
                last.next = curr
                last = last.next  
                
            
            curr = curr.next 
        
        last.next = None 
        return dummy.next
    