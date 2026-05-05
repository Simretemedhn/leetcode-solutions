"""class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        
        beginWord

        q = deque()
        q.append(beginWord)
        visited = set()
        #visited.add(beginWord)
        def differeByOne(arr1, arr2):
            arr1_s = set(arr1)
            arr2_s = set(arr2)

            return len(arr1_s - arr2_s) == 1

        level = 0
        while q:  
            n = len(q)
            level += 1 
            for _ in range(n):
                curr = q.popleft() 
                next_curr = curr
                for word in wordList:
                    if word not in visited and differeByOne(curr, word):
                        if word == endWord:
                            return level + 1 
                        visited.add(word)
                        q.append(word)
                        next_curr  = word 
                if next_curr == curr:
                    return 0
                    break 
                    
        return level 
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)  # Convert to set for O(1) lookup
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)  # FIXED: Mark start as visited
        
        def differByOne(word1, word2):
            diff = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        
        level = 1  # Start at 1 (beginWord counts as level 1)
        
        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                
                if curr == endWord:
                    return level
                
                for word in wordList:  # Still O(n²) but at least correct
                    if word not in visited and differByOne(curr, word):
                        visited.add(word)
                        q.append(word)
            
            level += 1
        
        return 0

        