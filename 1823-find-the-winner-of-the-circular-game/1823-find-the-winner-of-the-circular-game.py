class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        first = ListNode(1)
        prev = first
        

        for i in range(2, n+1):
            prev.next = ListNode(i)

            prev = prev.next 
        prev.next = first


        remaining  = n 
        while remaining > 1:

            for _ in range(k-1):
                prev = prev.next 
            prev.next = prev.next.next
            remaining -= 1 
        
        return prev.val 

