class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, count, right  = 0, 0, len(people)-1
        while left <= right:
            if people[right] + people[left] <= limit:   
                left += 1
                right -= 1
            else:
                right -= 1
            count +=1
        return count 
        