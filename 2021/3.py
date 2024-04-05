bonuses_sum = 0

while True:
    name = input()
    if name == "stop":
        break
    numbers = [int(x) for x in input().split(", ")]
    bonus = 1
    for num in numbers:
        bonus *= num
    bonuses_sum += bonus
    print(f"{name} has a bonus of {bonus} lv.")

print(f"The amount of all bonuses is {bonuses_sum} lv.")
