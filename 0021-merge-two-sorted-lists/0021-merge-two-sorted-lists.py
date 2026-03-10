# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        last = dummy
        curr1, curr2 = list1, list2 

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                dummy.next = curr1
                dummy = curr1
                curr1 = curr1.next
            else:
                dummy.next = curr2
                dummy = curr2
                curr2 = curr2.next
        while curr1:
            dummy.next = curr1
            dummy= curr1
            curr1 = curr1.next

        while curr2:
            dummy.next = curr2
            dummy= curr2
            curr2 = curr2.next
        return last.next