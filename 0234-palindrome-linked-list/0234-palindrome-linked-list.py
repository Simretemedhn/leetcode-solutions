# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # to find the middle one 
        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        # then reversing the second half 
        prev = None 
        curr = slow
        while curr:
            nex = curr.next
            curr.next = prev 
            prev = curr 
            curr = nex
        
        # checking equality of each node values 
        curr = head
        end = prev 
        while curr and end:
            if curr.val != end.val:
                return False 
            curr = curr.next
            end = end.next
        return True 