class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0


        visited = set()
        q = deque()  
        q.append("0000")
        visited.add("0000")

        def neighbours(num_in_str):
            collec = []
            nums = [int(ch) for ch in num_in_str]
            for i in range(4):
                nums[i] = (nums[i] + 1) % 10
                forward = "".join(map(str, nums))
                collec.append(forward)
                
                nums[i] = (nums[i] - 2) % 10  
                backward = "".join(map(str, nums))
                collec.append(backward)
                
                nums[i] = (nums[i] + 1) % 10  
            return collec 


        steps = 0 
        while q:

            n = len(q)
            steps += 1 

            for _ in range(n):
                node = q.popleft()
                if node not in deadends:
                    neis = neighbours(node)
                    for nei in neis:
                        if nei == target:
                            return steps
                        if nei not in visited and nei not in deadends:
                            q.append(nei)
                            visited.add(nei)
        
        return -1 

                    

