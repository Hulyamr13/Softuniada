class Color:
    def __init__(self, color):
        self.is_full = True
        self.color_text = color
        if color.startswith("("):
            self.is_full = False
            self.color_text = color[1:-1]

def main():
    n = int(input())
    for _ in range(n):
        first_sequence = [Color(x) for x in input().split()]
        target_sequence = [Color(x) for x in input().split()]
        matrix = [[False] * (len(target_sequence) + 1) for _ in range(len(first_sequence) + 1)]
        matrix[0][0] = True

        for first_index in range(len(first_sequence)):
            for target_index in range(len(target_sequence) + 1):
                if not matrix[first_index][target_index]:
                    continue

                if not first_sequence[first_index].is_full:
                    matrix[first_index + 1][target_index] = True

                if (first_sequence[first_index].is_full and target_index < len(target_sequence) and
                        first_sequence[first_index].color_text == target_sequence[target_index].color_text):
                    matrix[first_index + 1][target_index + 1] = True

                if (not first_sequence[first_index].is_full and target_index < len(target_sequence) and
                        first_sequence[first_index].color_text == target_sequence[target_index].color_text):
                    matrix[first_index + 1][target_index + 1] = True

        print("true" if matrix[len(first_sequence)][len(target_sequence)] else "false")

if __name__ == "__main__":
    main()
