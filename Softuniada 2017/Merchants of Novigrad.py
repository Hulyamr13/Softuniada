class Novigrad:
    graph = {}
    reverse_graph = {}
    cycle_nodes = set()
    reachable_from_end = []
    visited = []
    on_path = set()
    paths = []
    has_infinity_cycle = False
    has_cycle = False

    @staticmethod
    def find_coverage(start):
        Novigrad.reachable_from_end[start] = True
        for child in Novigrad.reverse_graph[start]:
            if not Novigrad.reachable_from_end[child]:
                Novigrad.find_coverage(child)

    @staticmethod
    def dfs(start):
        if Novigrad.has_infinity_cycle:
            return
        Novigrad.on_path.add(start)
        Novigrad.visited[start] = True
        for child in Novigrad.graph[start]:
            if child in Novigrad.on_path:
                Novigrad.has_cycle = True
                if Novigrad.reachable_from_end[child]:
                    Novigrad.has_infinity_cycle = True
                    return
            if not Novigrad.visited[child]:
                Novigrad.dfs(child)

            Novigrad.paths[start] = (Novigrad.paths[start] + Novigrad.paths[child]) % 1000000000
        Novigrad.on_path.remove(start)

    @staticmethod
    def main():
        tokens = input().split()
        vertices = int(tokens[0])
        roads = int(tokens[1])
        Novigrad.paths = [0] * (vertices + 1)
        Novigrad.reachable_from_end = [False] * (vertices + 1)
        Novigrad.visited = [False] * (vertices + 1)
        for i in range(1, vertices + 1):
            Novigrad.graph[i] = []
            Novigrad.reverse_graph[i] = []
        for _ in range(roads):
            edge_tokens = input().split()
            parent = int(edge_tokens[0])
            child = int(edge_tokens[1])
            Novigrad.graph[parent].append(child)
            Novigrad.reverse_graph[child].append(parent)
        Novigrad.find_coverage(vertices)
        Novigrad.paths[vertices] = 1
        Novigrad.dfs(1)

        if Novigrad.has_infinity_cycle:
            print("infinite")
        else:
            print(Novigrad.paths[1], "yes" if Novigrad.has_cycle else "no")


if __name__ == "__main__":
    Novigrad.main()
