# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(node1, node2, incoming):
            if not node1:
                incoming.next = node2
            elif not node2:
                incoming.next = node1 
            else:
                if node1.val < node2.val:
                    incoming.next = node1
                    merge(node1.next, node2, incoming.next)
                else:
                    incoming.next = node2 
                    merge(node1, node2.next, incoming.next)
                
        dummy = ListNode(0)
        final = dummy
        merge(list1, list2, final)
        return dummy.next 
            