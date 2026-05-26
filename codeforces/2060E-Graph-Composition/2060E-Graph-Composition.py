def find(parent, num):
        if parent[num] != num:
            parent[num] = find(parent, parent[num])
        return parent[num]
    
    def union(parent, rank, x, y):
        px = find(parent, x)
        py = find(parent, y)
        
        if px == py:
            return 
        
        if rank[px] > rank[py]:
            parent[py] = px 
        elif rank[py] > rank[px]:
            parent[px] = py 
        else:
            parent[px] = py 
            rank[py] += 1 
    
    f_edges = []
    for _ in range(edge_f):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        f_edges.append([u, v])
        
    g_edges = []
    for _ in range(edge_g):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        union(parent_g, rank_g, u, v)
        g_edges.append([u, v])
    
    count = 0
    
    # Process F edges
    for src, dst in f_edges:
        if find(parent_g, src) != find(parent_g, dst):
            count += 1  # remove this edge
        else:
            union(parent_f, rank_f, src, dst)  # keep this edge
    
    # NEW CODE: Count F-components inside each G-component
    from collections import defaultdict
    g_to_f_sets = defaultdict(set)
    
    for v in range(vertex):
        g_root = find(parent_g, v)
        f_root = find(parent_f, v)
        g_to_f_sets[g_root].add(f_root)
    
    # Add needed connections
    for g_root, f_roots in g_to_f_sets.items():
        count += len(f_roots) - 1
    
    print(count)