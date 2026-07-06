# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # brute force method 
        hash_Set = set()
        curr = head 
        while curr:
            if curr in hash_Set:
                return True 
            else:
                hash_Set.add(curr)
            curr = curr.next 
        return False 
