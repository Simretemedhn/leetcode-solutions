class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def next_index(i):
            return (i + nums[i]) % n
        
        for i in range(n):
            slow = fast = i
            
            # Phase 1: Find intersection
            while True:
                slow = next_index(slow)
                fast = next_index(next_index(fast))
                if slow == fast:
                    break
            
            # Phase 2: Find cycle start and length
            slow = i
            while slow != fast:
                slow = next_index(slow)
                fast = next_index(fast)
            
            # Phase 3: Validate cycle
            start = slow
            length = 0
            all_same_sign = True
            sign = nums[start] > 0
            
            curr = start
            while True:
                length += 1
                curr = next_index(curr)
                
                # Check if all have same sign
                if (nums[curr] > 0) != sign:
                    all_same_sign = False
                    
                if curr == start:
                    break
            
            if length > 1 and all_same_sign:
                return True
        
        return False