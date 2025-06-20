import json

def edmonds_karp(graph, source, sink):
    parent = {vertex: None for vertex in graph}
    max_flow = 0

    def bfs(source, sink):
        visited = set()
        queue = [source]
        visited.add(source)
        while queue:
            u = queue.pop(0)
            for v in graph[u]:
                if v not in visited and graph[u][v] > 0:
                    parent[v] = u
                    if v == sink:
                        return True
                    queue.append(v)
                    visited.add(v)
        return False

    while bfs(source, sink):
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

with open('./config.json', 'r') as f:
    graph = json.load(f)

print(edmonds_karp(graph['graph'], 'A', 'N'))