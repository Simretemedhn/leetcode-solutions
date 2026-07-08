# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # n"th node from the end means len(list) - n + 1  'th from the front (at the index of len(list)-n)

        # finding the length first 
        length = 0 
        curr = head 
        while curr:
            length +=  1 
            curr = curr.next 
        index  = length - n 
        
        # deleting at specific index 
        dummy = ListNode(0, head)
        curr =  dummy 
        for _ in range(index):
            curr = curr.next 
        curr.next = curr.next.next 
        return dummy.next 

