def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA != rootB:
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        elif rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        else:
            parent[rootB] = rootA
            rank[rootA] += 1
        return True
    return False

def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    rank = [0] * n
    mst_cost = 0
    edges_used = 0

    for u, v, cost in costs:
        if union(parent, rank, u, v): 
            mst_cost += cost
            edges_used += 1
        if edges_used == n - 1:
            break
    
    return mst_cost
