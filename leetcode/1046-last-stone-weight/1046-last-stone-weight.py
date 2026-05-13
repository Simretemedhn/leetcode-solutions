class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def swap(i, j):
            stones[i], stones[j] = stones[j], stones[i]
            
        def heap_down(ind, size):  
            left_child = 2 * ind + 1 
            right_child = 2 * ind + 2 
            largest_ind = ind 

            if left_child < size and stones[left_child] > stones[largest_ind]:
                largest_ind = left_child 
            if right_child < size and stones[right_child] > stones[largest_ind]:
                largest_ind = right_child 
            if largest_ind != ind:
                swap(ind, largest_ind)
                heap_down(largest_ind, size)
        
        def heapify(size):
            for ind in range(size//2 - 1, -1, -1):
                heap_down(ind, size)
        
        def remove(size):
            removing = stones[0]
            stones[0] = stones[size - 1]  
            stones.pop()
            heap_down(0, size - 1)  
            return removing

        def parent(child):
            return (child - 1) // 2

        def heap_up(current):
            if current == 0:
                return 
            p = parent(current)
            if stones[p] < stones[current]:
                swap(p, current)
                heap_up(p)

        def add(num):
            stones.append(num)
            heap_up(len(stones) - 1)  

        heapify(len(stones))
        
        while len(stones) > 1:  
            size = len(stones)
            removed_1 = remove(size)
            removed_2 = remove(size - 1)  
            
            if removed_1 != removed_2:
                add(abs(removed_1 - removed_2))
        
        return stones[0] if stones else 0