def repeat_str(s, count):
    return s * count

n = int(input())

first_row = repeat_str("_", n // 2 + 2) + "^" + repeat_str("_", n // 2 + 2)
print(first_row)

second_row = repeat_str("_", n // 2 + 1) + "/|\\" + repeat_str("_", n // 2 + 1)
print(second_row)

for i in range(n // 2 + 1):
    print(repeat_str("_", n // 2 - i) + "/" + repeat_str(".", i) + "|||" +
          repeat_str(".", i) + "\\" + repeat_str("_", n // 2 - i))

middle_row = "_/" + repeat_str(".", n // 2 - 1) + "|||" + repeat_str(".", n // 2 - 1) + "\\_"
print(middle_row)

for i in range(n):
    print(repeat_str("_", n // 2 + 1) + "|||" + repeat_str("_", n // 2 + 1))

down_middle_row = repeat_str("_", n // 2 + 1) + "~~~" + repeat_str("_", n // 2 + 1)
print(down_middle_row)

for i in range(n // 2):
    print(repeat_str("_", n // 2 - i) + "//" + repeat_str(".", i) +
          "!" + repeat_str(".", i) + "\\\\" + repeat_str("_", n // 2 - i))
