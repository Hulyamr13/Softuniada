def find_next(orders, stock, current_position):
    used_types = set()
    types_by_position = []
    for i in range(current_position + 1, len(orders)):
        if orders[i] in stock and orders[i] not in used_types:
            types_by_position.append(orders[i])
            used_types.add(orders[i])
    for item in stock:
        if item not in used_types:
            types_by_position.append(item)
    return types_by_position[-1]


def min_changes_to_fulfill_orders(stock_input, orders_input):
    stock = set(stock_input)
    types_count = {}

    for order in orders_input:
        types_count[order] = types_count.get(order, 0) + 1

    solution = True
    changes = 0

    for i in range(len(orders_input) - 1):
        if orders_input[i] not in stock:
            solution = False
            break

        if orders_input[i + 1] not in stock:
            item = find_next(orders_input, stock, i)
            stock.remove(item)
            stock.add(orders_input[i + 1])
            changes += 1

    if orders_input[-1] not in stock:
        solution = False

    return changes if solution else "impossible"


stock_input = list(map(int, input().split()))
orders_input = list(map(int, input().split()))

result = min_changes_to_fulfill_orders(stock_input, orders_input)
print(result)
