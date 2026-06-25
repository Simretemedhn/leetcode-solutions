class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Group indices by their value
        pairs = {}
        for i in range(len(nums)):
            if nums[i] in pairs:
                pairs[nums[i]].append(i)
            else:
                pairs[nums[i]] = [i]
        
        count = 0
        for pair in pairs:
            duplicates = pairs[pair]  # list of indices where this value appears
            n = len(duplicates)
            if n > 1:
                for i in range(n):
                    for j in range(i + 1, n):
                        if (duplicates[i] * duplicates[j]) % k == 0:
                            count += 1
        return count