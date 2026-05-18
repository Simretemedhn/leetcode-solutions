from collections import Counter, defaultdict 
from heapq import heappush, heappop, heapify 

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_cnt = Counter(words)
        word_list = defaultdict(list)
        for word, cnt in word_cnt.items():
            word_list[cnt].append(word) 

        sorted_one = dict(sorted(word_list.items(), reverse = True))
        result = [] 
        count_ = 0 
        found = False 
        for num, lists in sorted_one.items():
            heapq.heapify(lists)
            while lists:
                result.append(heapq.heappop(lists))
                count_ += 1 
                if count_ == k:
                    found = True 
                    break 
            if found:
                break 
        return result 

        
