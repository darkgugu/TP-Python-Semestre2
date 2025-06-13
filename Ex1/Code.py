import json
from collections import defaultdict


# importation du fichier json
with open("config.json", "r") as f:
    data = json.load(f)

nodes = data["nodes"]
edges = data["edges"]

# pour construire le graphe
graph = defaultdict(set)
for edge in edges:
    u, v = edge["from"], edge["to"]
    graph[u].add(v)
    graph[v].add(u)

# algo dfs & son test
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

print("DFS :")
for node in nodes:
    print(f"\nDepuis {node} :")
    dfs(graph, node)

def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex] - set(visited))
    return visited


print("BFS :")
for node in nodes:
    print(f"\nDepuis {node} :")
    result = bfs(graph, node)
    print(result)
