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
        if curr1:
            dummy.next = curr1

        if curr2:
            dummy.next = curr2
        
        return last.next 


"""
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:  
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy.next  """
    