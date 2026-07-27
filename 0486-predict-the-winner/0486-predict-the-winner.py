class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def compare(start, end):
            # If only 2 elements left, pick the larger one
            if end == start + 1:
                if nums[end] > nums[start]:
                    return end
                else:
                    return start
            
            # For optimal greedy: pick the one that gives better future
            # Compare what we get now vs what opponent might get next
            left_value = nums[start]
            right_value = nums[end]
            
            # If I take left, opponent can take max(nums[start+1], nums[end])
            if start + 1 <= end:
                opponent_if_left = max(nums[start + 1], nums[end])
            else:
                opponent_if_left = 0
                
            # If I take right, opponent can take max(nums[start], nums[end-1])
            if start <= end - 1:
                opponent_if_right = max(nums[start], nums[end - 1])
            else:
                opponent_if_right = 0
            
            # My advantage if I take left
            advantage_left = left_value - opponent_if_left
            # My advantage if I take right
            advantage_right = right_value - opponent_if_right
            
            # Choose the move that gives better advantage
            if advantage_left >= advantage_right:
                return start
            else:
                return end
        
        player_1 = 0
        player_2 = 0
        start = 0
        end = len(nums) - 1
        
        # Fixed: number of pairs of turns
        turns = len(nums) // 2
        
        for _ in range(turns):
            # Player 1's turn
            best_choice = compare(start, end)
            if best_choice == start:
                player_1 += nums[start]
                start += 1
            else:
                player_1 += nums[end]
                end -= 1
            
            # Player 2's turn (only if elements remain)
            if start <= end:
                best_choice = compare(start, end)
                if best_choice == start:
                    player_2 += nums[start]
                    start += 1
                else:
                    player_2 += nums[end]
                    end -= 1
        
        # If odd number of elements, Player 1 gets the last one
        if start == end:
            player_1 += nums[start]
        
        return player_1 >= player_2
"""

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        # i dont want to reveal the value where there is greater different from what i currently have 

        def compare(start, end):
            if end == start + 1:
                # return the indice of the maximuim value 
                if nums[end] > nums[start]:
                    return end 
                else:
                    return start 
            else:
                # compare with the previous of each indice then take the one with least loss 
                left_different = nums[start + 1] - nums[start]
                right_different = nums[end - 1] - nums[end]

                if left_different < right_different:
                    return start 
                else:
                    return end 
        
        player_1 = 0 
        player_2 = 0 
        start = 0 
        end  = len(nums) - 1
        turn = len(nums) + 1//2
        while turn:
            best_choice = compare(start, end)
            if best_choice == start:
                player_1 += nums[start]
                start += 1 
            else:
                player_1 += nums[end]
                end -= 1 

            best_choice = compare(start, end)
            if best_choice == start:
                player_2 += nums[start]
                start += 1 
            else:
                player_2 += nums[end]
                end -= 1 
            turn -= 1 
        """

                