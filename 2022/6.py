def get_height(figures):
    n = len(figures)
    heights = [0] * n

    for i in range(n):
        for j in range(i):
            if (figures[j][1] > figures[i][1] and figures[j][2] > figures[i][2]) or \
               (figures[j][1] > figures[i][2] and figures[j][2] > figures[i][1]):
                heights[i] = max(heights[i], heights[j])

        heights[i] += figures[i][0]

    return max(heights)

n = int(input())
figures = []
for _ in range(n):
    height, width, depth = map(int, input().split())
    # Добавяме всички възможни ротации на текущата фигура към списъка с фигури
    figures.append((height, width, depth))
    figures.append((height, depth, width))
    figures.append((width, height, depth))
    figures.append((width, depth, height))
    figures.append((depth, height, width))
    figures.append((depth, width, height))

print(get_height(figures))
