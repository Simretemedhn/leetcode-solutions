# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        
        # Step 1: Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # middle is slow. The second half starts at slow.next
        second_half_start = slow.next
        slow.next = None  # ← CRITICAL FIX: Disconnect the first half from the second half
        
        # Step 2: Reverse the second half
        prev = None
        curr = second_half_start
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        head2 = prev  # Start of reversed second half
        
        # Step 3: Merge the two halves
        move1 = head
        move2 = head2
        
        while move2:  # Second half is always shorter or equal now
            move1_next = move1.next
            move2_next = move2.next
            
            move1.next = move2
            move2.next = move1_next
            
            move1 = move1_next
            move2 = move2_next
            
