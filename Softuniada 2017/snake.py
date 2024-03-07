POINTS = 0

def move_snake(command):
    global POINTS
    move_points = 0
    if snake["direction"] == "up":
        for step in range(command[1]):
            snake["floor"] -= 1
            move_points += check_cell()
            if snake["status"] == 0:
                break
    elif snake["direction"] == "down":
        for step in range(command[1]):
            snake["floor"] += 1
            move_points += check_cell()
            if snake["status"] == 0:
                break
    elif snake["direction"] == "forward":
        for step in range(command[1]):
            snake["row"] -= 1
            move_points += check_cell()
            if snake["status"] == 0:
                break
    elif snake["direction"] == "backward":
        for step in range(command[1]):
            snake["row"] += 1
            move_points += check_cell()
            if snake["status"] == 0:
                break
    elif snake["direction"] == "left":
        for step in range(command[1]):
            snake["col"] -= 1
            move_points += check_cell()
            if snake["status"] == 0:
                break
    elif snake["direction"] == "right":
        for step in range(command[1]):
            snake["col"] += 1
            move_points += check_cell()
            if snake["status"] == 0:
                break
    snake["direction"] = command[0]
    return move_points

def check_cell():
    global POINTS
    try:
        cell_value = cube[snake["floor"]][snake["row"]][snake["col"]]
        if cell_value == "a":
            cube[snake["floor"]][snake["row"]][snake["col"]] = "o"
            return 1
        else:
            return 0
    except IndexError:
        snake["status"] = 0
        return 0

if __name__ == '__main__':
    size = int(input())
    cube = [[] for x in range(size)]

    for matrix in range(size):
        floor_rows = [[c for c in row] for row in input().split(" | ")]
        for floor in range(size):
            cube[floor].append(floor_rows[floor])

    snake = {
        'floor': 0,
        'row': 0,
        'col': 0,
        'direction': "",
        'status': 1
    }

    snake["direction"] = input()
    commands = []

    while True:
        command = input().split(" ")
        commands.append([command[0], int(command[2])])
        if command[0] == "end":
            break

    for floor in range(size):
        for row in range(size):
            col = False
            if "s" in cube[floor][row]:
                col = cube[floor][row].index("s")
            if col:
                snake["floor"] = floor
                snake["row"] = row
                snake["col"] = col

    for com in commands:
        POINTS += move_snake(com)
        if snake['status'] == 0:
            break

    print("Points collected: {}".format(POINTS))
    if snake['status'] == 0:
        print("The snake dies.")
