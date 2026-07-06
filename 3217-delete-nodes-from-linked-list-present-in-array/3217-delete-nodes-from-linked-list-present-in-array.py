# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        set_nums = set(nums)
        dummy = ListNode(0)
        dummy.next = head 
        curr = dummy

        while curr.next:
            if curr.next.val in set_nums:
                curr.next = curr.next.next 
            else:
                curr = curr.next 
        return dummy.next 
