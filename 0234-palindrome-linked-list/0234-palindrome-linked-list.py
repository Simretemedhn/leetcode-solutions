# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next 
        origin = stack.copy()

        reverse = []
        while stack:
            reverse.append(stack.pop())
        return origin == reverse 

        