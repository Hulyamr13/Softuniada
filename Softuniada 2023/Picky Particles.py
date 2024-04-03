def main():
    n = int(input())

    p_graph = {}
    e_graph = {}
    p_pairs = {}
    e_pairs = {}
    merged = [False] * n

    for i in range(n):
        pref = list(map(int, input().split()))
        p_graph[i] = pref

    for i in range(n):
        pref = list(map(int, input().split()))
        e_graph[i] = pref

    while len(p_pairs) < n:
        p = -1

        for p in range(len(merged)):
            if not merged[p]:
                break

        if p < 0 or p >= n:
            break

        e = p_graph[p].pop(0)

        if e not in e_pairs:
            p_pairs[p] = e
            e_pairs[e] = p
            merged[p] = True
        else:
            p_old = e_pairs[e]
            p_new = p
            pref = find_pref(e_graph[e], p_old, p_new)

            if pref == p_new:
                del p_pairs[e_pairs[e]]
                merged[e_pairs[e]] = False
                e_pairs[e] = p
                p_pairs[p] = e
                merged[p] = True

    for i in range(n):
        print(f"{i} <-> {p_pairs.get(i)}")


def find_pref(integers, p_old, p_new):
    for integer in integers:
        if integer == p_old:
            return p_old
        elif integer == p_new:
            return p_new

    return -1


if __name__ == "__main__":
    main()
