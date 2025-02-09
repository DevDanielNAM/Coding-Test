def solution(info, edges):
    from collections import defaultdict

    tree = defaultdict(list)
    for parent, child in edges:
        tree[parent].append(child)

    def dfs(current, sheep, wolf, next_nodes):
        nonlocal max_sheep
        if info[current]:
            wolf += 1
        else:
            sheep += 1

        if wolf >= sheep:
            return
        
        max_sheep = max(max_sheep, sheep)

        for next_node in tree[current]:
            next_nodes.append(next_node)

        for i, next_node in enumerate(next_nodes):
            dfs(next_node, sheep, wolf, next_nodes[:i] + next_nodes[i+1:])

    max_sheep = 0
    dfs(0, 0, 0, [])
    return max_sheep
