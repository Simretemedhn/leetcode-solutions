# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        
        less = less_dummy
        great = greater_dummy

        curr = head 
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                great.next = curr
                great = great.next
            curr = curr.next

        great.next = None 
        less.next = greater_dummy.next
        return less_dummy.next
      