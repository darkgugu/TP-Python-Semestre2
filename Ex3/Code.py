import json


def load_graph_from_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    edges = data["edges"]
    source = data["source"]
    return edges, source


def bellman_ford(edges, source):
    vertices = set()
    for edge in edges:
        vertices.add(edge["from"])
        vertices.add(edge["to"])

    distance = {v: float("inf") for v in vertices}
    parent = {v: None for v in vertices}
    distance[source] = 0

    for _ in range(len(vertices) - 1):
        for edge in edges:
            u, v, w = edge["from"], edge["to"], edge["weight"]
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u

    has_negative_cycle = False
    for edge in edges:
        u, v, w = edge["from"], edge["to"], edge["weight"]
        if distance[u] + w < distance[v]:
            has_negative_cycle = True
            break

    return distance, parent, has_negative_cycle


if __name__ == "__main__":
    edges, source = load_graph_from_json("config.json")
    distances, parents, has_cycle = bellman_ford(edges, source)

    print("Distances depuis la source :", distances)
    print("Parents :", parents)
    print("Cycle de poids négatif :", "Oui" if has_cycle else "Non")
