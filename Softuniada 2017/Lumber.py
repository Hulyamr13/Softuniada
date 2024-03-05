class Stick:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    rank = [0] * 1001
    parent = [i for i in range(1001)]
    sticks = [None] * 1001
    output = []

    def find_set(node):
        root = node
        while parent[root] != root:
            root = parent[root]
        return root

    def union(a, b):
        root_a = find_set(a)
        root_b = find_set(b)
        if rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        elif rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_b] = root_a
            rank[root_a] += 1

    def is_same_set(a, b):
        return find_set(a) == find_set(b)

    def intersect(a, b):
        return (a.top_left.x <= b.bottom_right.x and
                b.top_left.x <= a.bottom_right.x and
                a.top_left.y >= b.bottom_right.y and
                b.top_left.y >= a.bottom_right.y)

    data = input().split(' ')
    n, m = map(int, data)
    for j in range(1, n + 1):
        log_data = input().split(' ')
        top_left_x, top_left_y, bottom_right_x, bottom_right_y = map(int, log_data)
        sticks[j] = Stick(Point(top_left_x, top_left_y), Point(bottom_right_x, bottom_right_y))
        parent[j] = j
        rank[j] = 0
        for p in range(1, j):
            if not is_same_set(j, p) and intersect(sticks[j], sticks[p]):
                union(j, p)

    for _ in range(m):
        query_data = input().split(' ')
        start, end = map(int, query_data)
        output.append("YES" if is_same_set(start, end) else "NO")

    print("\n".join(output))

if __name__ == "__main__":
    main()
