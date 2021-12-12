def solve(G):
    def rec(v, p):
        nonlocal G, visited, paths_cnt

        if v == 'end':
            paths_cnt += 1
            return

        if visited[v] == 0 or v.isupper():
            visited[v] = 1
            for u in G[v]:
                rec(u, v)

            visited[v] = 0

    visited = {v: 0 for v in G}
    paths_cnt = 0

    rec('start', None)

    return paths_cnt


with open('12_i.txt') as f:
    A = f.read().splitlines()

    def add_edge(G, u, v):
        if u in G:
            G[u].add(v)
        else:
            G[u] = {v}

    G = {}
    for l in A:
        u, v = l.split('-')
        add_edge(G, u, v)
        add_edge(G, v, u)

print(solve(G))
