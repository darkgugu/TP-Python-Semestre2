import json
from collections import defaultdict

# importation du fichier json
with open("config.json", "r") as f:
    data = json.load(f)

nodes = data["nodes"]
edges = data["edges"]

# construction du graphe (non orienté)
graph = defaultdict(set)
for edge in edges:
    u, v = edge["from"], edge["to"]
    graph[u].add(v)
    graph[v].add(u)

# DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

print("DFS :")
for node in nodes:
    print(f"\nDepuis {node} :")
    dfs(graph, node)
    print()

# BFS
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

# Détection de cycle avec DFS
def detect_cycle_dfs(graph):
    visited = set()

    def dfs_cycle(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs_cycle(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs_cycle(node, None):
                return True
    return False

print("\nCycle détecté dans le graphe ?", detect_cycle_dfs(graph))

# Composantes connexes avec BFS
def connected_components_bfs(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            queue = [node]
            while queue:
                current = queue.pop(0)
                if current not in visited:
                    visited.add(current)
                    component.append(current)
                    queue.extend(graph[current] - visited)
            components.append(component)
    return components

print("\nComposantes connexes :", connected_components_bfs(graph))
