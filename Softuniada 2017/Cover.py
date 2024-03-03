from collections import deque
import math

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

class ShelterBinary:
    work = []
    bfsDist = []
    capacity = 0
    endNode = 0
    edges = []
    capacities = []
    distanceMatrix = []

    @staticmethod
    def main():
        tokens = input().split()
        soldiersCount = int(tokens[0])
        bunkersCount = int(tokens[1])
        ShelterBinary.capacity = int(tokens[2])
        soldiers = [None] * (soldiersCount + 1)

        for i in range(1, soldiersCount + 1):
            soldierTokens = input().split()
            x = int(soldierTokens[0])
            y = int(soldierTokens[1])
            soldiers[i] = Point(x, y)

        ShelterBinary.distanceMatrix = [[0] * (soldiersCount + 1) for _ in range(bunkersCount + 1)]

        for i in range(1, bunkersCount + 1):
            bunkerTokens = input().split()
            for j in range(1, soldiersCount + 1):
                x = int(bunkerTokens[0])
                y = int(bunkerTokens[1])
                distanceX = x - soldiers[j].X
                distanceY = y - soldiers[j].Y
                distance = distanceX * distanceX + distanceY * distanceY
                ShelterBinary.distanceMatrix[i][j] = distance

        ShelterBinary.endNode = soldiersCount + bunkersCount + 1
        ShelterBinary.work = [0] * (ShelterBinary.endNode + 1)
        ShelterBinary.bfsDist = [-1] * (ShelterBinary.endNode + 1)
        ShelterBinary.capacities = [[0] * (ShelterBinary.endNode + 1) for _ in range(ShelterBinary.endNode + 1)]

        distances = sorted(set(distance for row in ShelterBinary.distanceMatrix[1:] for distance in row[1:]))
        bestDistance = distances[-1]

        low, high = 0, len(distances) - 1
        while low <= high:
            mid = (low + high) // 2
            res = ShelterBinary.dinic_constrained(distances[mid], soldiersCount, bunkersCount)
            if res == soldiersCount:
                bestDistance = min(bestDistance, distances[mid])
                high = mid - 1
            else:
                low = mid + 1

        print("{0:.6f}".format(math.sqrt(bestDistance)))

    @staticmethod
    def dinic_constrained(max_weight, soldiers_count, bunkers_count):
        ShelterBinary.edges = [[] for _ in range(ShelterBinary.endNode + 1)]

        for i in range(1, soldiers_count + 1):
            ShelterBinary.edges[0].append(i)
            ShelterBinary.edges[i].append(0)
            ShelterBinary.capacities[0][i] = 1

        ShelterBinary.edges[ShelterBinary.endNode] = []
        for i in range(1, bunkers_count + 1):
            ShelterBinary.edges[soldiers_count + i].append(ShelterBinary.endNode)
            ShelterBinary.edges[ShelterBinary.endNode].append(soldiers_count + i)
            ShelterBinary.capacities[soldiers_count + i][ShelterBinary.endNode] = ShelterBinary.capacity

            for j in range(1, soldiers_count + 1):
                if ShelterBinary.distanceMatrix[i][j] <= max_weight:
                    ShelterBinary.edges[j].append(soldiers_count + i)
                    ShelterBinary.edges[soldiers_count + i].append(j)
                    ShelterBinary.capacities[j][soldiers_count + i] = 1

        return ShelterBinary.dinic(0, ShelterBinary.endNode)

    @staticmethod
    def dinic(source, destination):
        result = 0
        while ShelterBinary.bfs(source, destination):
            ShelterBinary.work = [0] * (ShelterBinary.endNode + 1)
            delta = 0
            while True:
                delta = ShelterBinary.dfs(source, destination, float('inf'))
                if delta == 0:
                    break
                result += delta
        return result

    @staticmethod
    def bfs(src, dest):
        ShelterBinary.bfsDist = [-1] * (ShelterBinary.endNode + 1)
        ShelterBinary.bfsDist[src] = 0
        queue = deque([src])
        while queue:
            currentNode = queue.popleft()
            for child in ShelterBinary.edges[currentNode]:
                if ShelterBinary.bfsDist[child] < 0 and ShelterBinary.capacities[currentNode][child] > 0:
                    ShelterBinary.bfsDist[child] = ShelterBinary.bfsDist[currentNode] + 1
                    queue.append(child)
        return ShelterBinary.bfsDist[dest] >= 0

    @staticmethod
    def dfs(source, destination, flow):
        if source == destination:
            return flow
        while ShelterBinary.work[source] < len(ShelterBinary.edges[source]):
            child = ShelterBinary.edges[source][ShelterBinary.work[source]]
            if ShelterBinary.capacities[source][child] <= 0:
                ShelterBinary.work[source] += 1
                continue
            if ShelterBinary.bfsDist[child] == ShelterBinary.bfsDist[source] + 1:
                augmentation_path_flow = ShelterBinary.dfs(child, destination, min(flow, ShelterBinary.capacities[source][child]))
                if augmentation_path_flow > 0:
                    ShelterBinary.capacities[source][child] -= augmentation_path_flow
                    ShelterBinary.capacities[child][source] += augmentation_path_flow
                    return augmentation_path_flow
            ShelterBinary.work[source] += 1
        return 0

if __name__ == "__main__":
    ShelterBinary.main()
