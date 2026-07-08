class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        # Find lengths
        curr = headA
        a_len = 0  
        while curr:
            a_len += 1 
            curr = curr.next 

        curr = headB 
        b_len = 0 
        while curr:
            b_len += 1 
            curr = curr.next 
        
        # Align pointers
        p1, p2 = headA, headB
        
        if a_len > b_len:
            shift = a_len - b_len
            for _ in range(shift):
                p1 = p1.next
        else:
            shift = b_len - a_len
            for _ in range(shift):
                p2 = p2.next
        
        # Compare nodes
        while p1 and p2:
            if p1 == p2:  
                return p1
            p1 = p1.next
            p2 = p2.next
        
        return None


