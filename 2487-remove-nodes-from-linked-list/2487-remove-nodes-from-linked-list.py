# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # we better first build an array from the given linked list then reverse it based on inceasing order while building linked list 

        array_Version = []   
        curr = head 
        while curr:
            array_Version.append(curr.val)   
            curr = curr.next 
        array_Version.reverse()

        biggest = array_Version[0]
        increasing_array = [biggest] 
        for i in range(1, len(array_Version)):
            if array_Version[i] >= biggest:
                biggest = array_Version[i]
                increasing_array.append(array_Version[i])
        
        increasing_array.reverse()



        dummy = ListNode(increasing_array[0])
        curr = dummy 

        for i in range(1, len(increasing_array)):
            next_elem = ListNode(increasing_array[i])
            curr.next = next_elem
            curr = next_elem 
        return dummy 
            
