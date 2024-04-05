def main():
    n = int(input())  # Брой елементи
    elements = [str(x) for x in range(1, n + 1)]

    m = int(input())  # Брой зависимости
    dependencies = []

    for _ in range(m):
        dependency = input().split(" > ")
        dependencies.append((dependency[0], dependency[1]))

    permutations = set()

    def get_permutations(idx, permutation):
        if idx == n:
            permutations.add(tuple(permutation))
            return

        for element in elements:
            if element not in permutation:
                permutation[idx] = element
                get_permutations(idx + 1, permutation.copy())

    get_permutations(0, [""] * n)

    def dependencies_are_right(perm):
        for dependency in dependencies:
            idx1 = perm.index(dependency[0])
            idx2 = perm.index(dependency[1])
            if idx1 < idx2:
                return False
        return True

    ans = sum(1 for perm in permutations if dependencies_are_right(perm))

    print(ans)

if __name__ == "__main__":
    main()
