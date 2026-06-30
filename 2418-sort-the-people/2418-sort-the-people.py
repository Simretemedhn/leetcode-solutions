class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        if not heights:
            return []
        
        # counting sort 
        # counting sort 

        min_val = min(heights)
        max_val = max(heights)
        
        count = [0] * (max_val - min_val + 1)
        for h in heights:
            count[h - min_val] += 1
        
        result = []
        for i in range(len(count) - 1, -1, -1):
            freq = count[i]
            if freq > 0:
                height = i + min_val
                # Find names with this height
                for _ in range(freq):
                    idx = heights.index(height)
                    result.append(names[idx])
                    heights[idx] = -1  # Mark as used
        
        return result

        # insertion sort 
        # insertion sort 

        n = len(heights)
        for i in range(1, n):
            key_height  = heights[i]
            key_name = names[i]
            j = i - 1 
            while j >= 0 and heights[j] < heights[i]:
                heights[j+1] = heights[j]
                names[j+1] = names[j]
                j -= 1 

            heights[j+1] = key_height
            names[j+1] = key_name
        return names 

        # selection sort
        # selection sort

        n = len(heights)
        for i in range(n):
            max_ind = i
            for j in range(i+1, n):
                if heights[j] > heights[max_ind]:
                    max_ind =  j 
            heights[i], heights[max_ind] = heights[max_ind], heights[i]
            names[i], names[max_ind] = names[max_ind], names[i] 
        return names 

        # bubble sorting (optimized version )
        # bubble sorting (optimized version )

        make_a_swap = True 
        n = len(heights)

        for i in range(n):
            swapped = False 
            for j in range(n-i-1):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
                    swapped = True 
            if not swapped:
                break 
        return names

        # buble sorting (optimized version using while loop)
        # buble sorting (optimized version using while loop)

        make_a_swap = True 
        n = len(heights)
        while make_a_swap:
            make_a_swap = False 
            for i in range(n-1):
                if heights[i] < heights[i+1]:
                    heights[i], heights[i+1] = heights[i+1], heights[i]
                    names[i], names[i+1] = names[i+1], names[i]
                    make_a_swap = True 
        return names 

        # bubble sort foundation concept 
        # bubble sort foundation concept  
        
        n = len(heights)
        for i in range(n):
            for j in range(n-i-1):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
        return nammes 
