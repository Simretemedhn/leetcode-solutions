class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Convert array to linked list
        dummy = ListNode(0)
        current = dummy
        
        # Build linked list from array (skip val)
        for num in nums:
            if num != val:
                current.next = ListNode(num)
                current = current.next
        
        # Count remaining nodes
        count = 0
        current = dummy.next
        while current:
            count += 1
            current = current.next
        
        # Convert back to array (in-place)
        i = 0
        current = dummy.next
        while current:
            nums[i] = current.val
            i += 1
            current = current.next
        
        # Fill rest with placeholder (not required but good practice)
        for i in range(count, len(nums)):
            nums[i] = '_'  # Or any placeholder
        
        return count