def find_root(node, parents):
    while node != parents[node]:
        node = parents[node]
    return node


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


def kruskal(vertex_count, edges):
    edges.sort(key=lambda x: x.weight)
    parents = [i for i in range(vertex_count)]
    min_weight = 0

    for edge in edges:
        first_root = find_root(edge.start, parents)
        second_root = find_root(edge.end, parents)

        if first_root != second_root:
            parents[first_root] = second_root
            min_weight = edge.weight

    return min_weight + 1


if __name__ == "__main__":
    vertex_count = int(input())
    edge_count = int(input())

    edges = []

    for _ in range(edge_count):
        start, end, weight = map(int, input().split())
        edges.append(Edge(start, end, weight))

    min_weight = kruskal(vertex_count, edges)
    print(min_weight)
