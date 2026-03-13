# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 

        curr = head
        odd = ListNode(0)
        odd_ = odd

        while curr and curr.next:
            odd_.next = curr.next
            odd_ = odd_.next
            if curr.next.next != None:
                curr.next = curr.next.next
                curr = curr.next
            else:
                break 
        odd_.next = None 
        curr.next = odd.next

        return head 
"""or shortly 
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        return head

"""