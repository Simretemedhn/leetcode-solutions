# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # for odd length, the element to be deleted is at (n - 1)//2 indice 
        # for even lenght, the element to be deleted is at exactly n//2 
    

        # let's first find the length
        length = 0 
        curr = head 
        while curr:
            length +=  1 
            curr = curr.next 

        if length == 1:
            return None 
        if length % 2 == 0:
            pos = length//2 
        else:
            pos = (length - 1)//2 
    
        current = head
        dummy  = head 
        indice = 0 
        while current and indice + 1  < pos:

            previous = current 
            current = current.next 
            indice += 1 
        current.next = current.next.next 
        
        return dummy
