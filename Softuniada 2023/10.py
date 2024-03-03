import heapq

class Vertex:
    def __init__(self, index, distance):
        self.index = index
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

def dijkstra(vertices, graph, potentials):
    previous = [-1] * len(vertices)
    for vertex in vertices:
        vertex.distance = float('inf')
    start = vertices[0]
    start.distance = 0
    priority_queue = [start]
    heapq.heapify(priority_queue)
    while priority_queue:
        current = heapq.heappop(priority_queue)
        for next_index, edge_weight in graph[current.index].items():
            neighbour = vertices[next_index]
            new_distance = current.distance + edge_weight + potentials[current.index] - potentials[next_index]
            if new_distance < neighbour.distance:
                neighbour.distance = new_distance
                previous[neighbour.index] = current.index
                heapq.heappush(priority_queue, neighbour)  # добавяме новата версия в опашката
    return previous

def main():
    vertex_count = int(input())
    edge_count = int(input())

    vertices = [Vertex(i, float('inf')) for i in range(vertex_count)]
    graph = [{} for _ in range(vertex_count)]
    paths = [set() for _ in range(vertex_count)]

    for _ in range(edge_count):
        start, end, weight = map(int, input().split())
        graph[start][end] = weight
        graph[end][start] = weight

    potentials = [0] * vertex_count
    previous = dijkstra(vertices, graph, potentials)
    store_path(graph, previous, paths)
    reverse_path(graph, previous)
    for i in range(len(potentials)):
        potentials[i] = vertices[i].distance
    previous = dijkstra(vertices, graph, potentials)
    store_path(graph, previous, paths)
    first_path = get_path(paths)
    second_path = get_path(paths)

    print(" -> ".join(map(str, first_path)))
    print(" -> ".join(map(str, second_path)))

def reverse_path(graph, previous):
    element = len(previous) - 1
    parent = previous[-1]
    while parent != -1:
        weight = graph[element][parent]
        del graph[element][parent]
        del graph[parent][element]

        graph[element][parent] = -weight
        element = parent
        parent = previous[parent]

def store_path(graph, previous, paths):
    element = len(previous) - 1
    parent = previous[-1]
    while parent != -1:
        if parent in paths[element]:
            paths[element].remove(parent)
        else:
            paths[parent].add(element)
        element = parent
        parent = previous[parent]

def get_path(paths):
    start = 0
    end = len(paths) - 1
    path = []
    cur = start
    while cur != end:
        path.append(cur)
        next_ = paths[cur].pop()
        cur = next_
    path.append(end)
    return path

if __name__ == "__main__":
    main()
