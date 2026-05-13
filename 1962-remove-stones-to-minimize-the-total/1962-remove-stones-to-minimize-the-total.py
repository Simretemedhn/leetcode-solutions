import math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:    
        n = len(piles)

        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
             
        def heapdown(heap, ind):
            left_child = 2 * ind + 1 
            right_child = 2 * ind + 2
            largest_ind = ind

            if left_child < n and heap[left_child] > heap[largest_ind]:
                largest_ind = left_child 
            if right_child < n and heap[right_child] > heap[largest_ind]:
                largest_ind = right_child 
            if largest_ind != ind:
                swap(heap, ind, largest_ind)
                heapdown(heap, largest_ind)
        
        for i in range((n-2)//2, -1, -1):
            heapdown(piles, i)

        for _ in range(k):
            piles[0] -= math.floor(piles[0] / 2)  
            heapdown(piles, 0)

        return sum(piles)