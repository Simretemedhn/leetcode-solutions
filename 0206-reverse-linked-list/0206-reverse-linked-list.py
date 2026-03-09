# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next     
            curr.next = prev
            prev = curr
            curr = next_temp
        
        return prev

"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            linked_to = curr
            curr = curr.next

            next_cur = curr.next
            curr.next = linked_to
            curr = next_cur
        head = curr
        return head

"""