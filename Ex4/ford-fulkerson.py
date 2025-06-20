import json

def ford_fulkerson(graph, source, sink):
    parent = {vertex: None for vertex in graph}
    max_flow = 0

    def dfs(u, visited):
        if u == sink:
            return True
        visited.add(u)
        for v in graph[u]:
            if v not in visited and graph[u][v] > 0:
                parent[v] = u
                if dfs(v, visited):
                    return True
        return False

    while True:
        visited = set()
        parent = {vertex: None for vertex in graph}
        if not dfs(source, visited):
            break

        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            if u not in graph[v]:
                graph[v][u] = 0
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow

with open('./Ex4/config.json', 'r') as f:
    graph = json.load(f)

print(ford_fulkerson(graph['graph'], 'A', 'F'))