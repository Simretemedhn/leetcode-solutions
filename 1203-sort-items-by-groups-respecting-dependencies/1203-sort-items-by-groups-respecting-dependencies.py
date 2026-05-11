from typing import List
from collections import defaultdict, deque

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        
        total_groups = group_id
        
        group_graph = defaultdict(set)
        group_indegree = [0] * total_groups
        
        item_graph = defaultdict(list)
        item_indegree = [0] * n
        
        for i in range(n):
            for before in beforeItems[i]:
                item_graph[before].append(i)
                item_indegree[i] += 1
                
                if group[before] != group[i]:
                    if group[i] not in group_graph[group[before]]:
                        group_graph[group[before]].add(group[i])
                        group_indegree[group[i]] += 1
        
        group_queue = deque()
        for g in range(total_groups):
            if group_indegree[g] == 0:
                group_queue.append(g)
        
        group_order = []
        while group_queue:
            curr_group = group_queue.popleft()
            group_order.append(curr_group)
            
            for next_group in group_graph[curr_group]:
                group_indegree[next_group] -= 1
                if group_indegree[next_group] == 0:
                    group_queue.append(next_group)
        
        if len(group_order) != total_groups:
            return []
        
        items_by_group = defaultdict(list)
        for i in range(n):
            items_by_group[group[i]].append(i)
        
        result = []
        
        for g in group_order:
            group_items = items_by_group[g]
            
            item_to_index = {item: idx for idx, item in enumerate(group_items)}
            
            local_graph = defaultdict(list)
            local_indegree = [0] * len(group_items)
            
            for i in group_items:
                for before in beforeItems[i]:
                    if group[before] == g:
                        from_idx = item_to_index[before]
                        to_idx = item_to_index[i]
                        local_graph[from_idx].append(to_idx)
                        local_indegree[to_idx] += 1
            
            local_queue = deque()
            for idx in range(len(group_items)):
                if local_indegree[idx] == 0:
                    local_queue.append(idx)
            
            local_order = []
            while local_queue:
                curr_idx = local_queue.popleft()
                local_order.append(group_items[curr_idx])
                
                for next_idx in local_graph[curr_idx]:
                    local_indegree[next_idx] -= 1
                    if local_indegree[next_idx] == 0:
                        local_queue.append(next_idx)
            
            if len(local_order) != len(group_items):
                return []
            
            result.extend(local_order)
        
        return result