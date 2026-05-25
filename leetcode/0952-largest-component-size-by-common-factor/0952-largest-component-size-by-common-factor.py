from collections import defaultdict, Counter
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        
        parent = list(range(n)) 
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
        
        def prime_factors(num):
            i = 2
            factors = set()
            n_temp = num
            while i * i <= n_temp:
                while n_temp % i == 0:
                    factors.add(i)
                    n_temp //= i
                i += 1
            if n_temp > 1:
                factors.add(n_temp)
            return factors
        
        prime_to_index = {}
        
        for i, num in enumerate(nums):
            factors = prime_factors(num)
            for factor in factors:
                if factor in prime_to_index:
                    union(i, prime_to_index[factor])
                else:
                    prime_to_index[factor] = i
        
        component_sizes = Counter()
        for i in range(n):
            root = find(i)
            component_sizes[root] += 1
        
        return max(component_sizes.values())


"""class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:


        def prime_factors(n):
            i = 2
            factors = []
            while i * i <= n:
                while n % i == 0:
                    factors.append(i)
                    n //= i
                i += 1
            if n > 1:
                factors.append(n)
            return factors

        for num in nums:
            factors = prime_factors(num)
            for every in factors:
                if every in mapping:
                    # find its parent node 
                    will_add = set(Factors) - mapping[every]
                    mapping[every].update(will_add)
        max_ = 0
        for parent in parents:
            root = find(parent)
            max_ = max(max_, len(mapping[root]))
        return max_ """

        