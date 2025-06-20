import json


def load_tsp(filepath="./Ex7/config.json"):
    with open(filepath, "r") as f:
        return json.load(f)["TSP"]


def tsp_nearest_neighbor(cities, dist_matrix, start=0):
    n = len(cities)
    visited = [False] * n
    path = [start]
    total_dist = 0
    current = start
    visited[start] = True

    for _ in range(n - 1):
        next_city = None
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and 0 < dist_matrix[current][i] < min_dist:
                min_dist = dist_matrix[current][i]
                next_city = i
        if next_city is not None:
            path.append(next_city)
            total_dist += min_dist
            visited[next_city] = True
            current = next_city

    total_dist += dist_matrix[current][start]  # Retour au départ
    path.append(start)
    return [cities[i] for i in path], total_dist


if __name__ == "__main__":
    data = load_tsp()
    cities = data["cities"]
    dist_matrix = data["distances"]

    path, cost = tsp_nearest_neighbor(cities, dist_matrix)
    print("Itinéraire TSP (heuristique):", path)
    print("Distance totale :", cost)
