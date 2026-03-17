# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = []
        curr = head 
        while curr:
            while stack and stack[-1] < curr.val:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next 
        print(stack)
        new_final = None 
        while stack:
            val = stack.pop()
            new_node = ListNode(val, new_final)
            new_node.next = new_final
            new_final = new_node 
        return new_final