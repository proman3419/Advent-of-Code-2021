def solve(G):
    def rec(v, p, visited_twice):
        nonlocal G, visited, paths_cnt

        if v == 'end':
            paths_cnt += 1
            return

        if visited[v] == 0 or v.isupper() or not visited_twice:
            if visited[v] == 1 and v.islower():
                visited_twice = True

            visited[v] += 1
            for u in G[v]:
                if u != 'start':
                    rec(u, v, visited_twice)

            visited[v] -= 1

    visited = {v: 0 for v in G}
    paths_cnt = 0

    rec('start', None, False)

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

    for k in G:
        G[k] = set(G[k])

print(solve(G))
