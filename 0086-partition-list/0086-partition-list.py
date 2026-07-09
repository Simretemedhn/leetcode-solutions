# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than = []
        greater_than = []

        curr = head 
        while curr:
            if curr.val < x:
                less_than.append(curr.val)
            elif curr.val > x:
                greater_than.append(curr.val)
        
        dummy = ListNode(0)
        last = dummy 
        for i in range(len(less_than)):
            new_node = ListNode(less_than[i])
            last.next = new_node 
            last = last.next 
        
        last.next = ListNode(x)
        last = last.next 
        for i in range(len(greater_than)):
            new_node = ListNode(greater_than[i])
            last.next = new_node 
            last = last.next 
        return dummy.next"""

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        
        less_than = []
        greater_than = []

        curr = head 
        while curr:
            if curr.val < x:
                less_than.append(curr.val)
            else:  # FIX 2: >= x goes to greater_than
                greater_than.append(curr.val)
            curr = curr.next  # FIX 3: Move forward!
        
        dummy = ListNode(0)
        last = dummy 
        
        for val in less_than:
            new_node = ListNode(val)
            last.next = new_node 
            last = last.next 
        
        for val in greater_than:
            new_node = ListNode(val)
            last.next = new_node 
            last = last.next 
        
        return dummy.next