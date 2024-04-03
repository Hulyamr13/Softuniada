import math

class ParkingSpace:
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y
        self.distance_from_target = self.calculate_distance_from_target(x, y, target_x, target_y)

    def calculate_distance_from_target(self, x, y, target_x, target_y):
        distance = (abs(x - target_x) + abs(y - target_y)) * 2 - 1
        return distance

    def __lt__(self, other):
        return self.distance_from_target < other.distance_from_target

class Zone:
    def __init__(self, name, x, y, length, width, price):
        self.name = name
        self.min_x = x
        self.min_y = y
        self.max_x = x + length
        self.max_y = y + width
        self.price_per_min = price
        self.best_parking_space = None

    def add_parking_space(self, parking_space):
        if self.best_parking_space is None or parking_space.distance_from_target < self.best_parking_space.distance_from_target:
            self.best_parking_space = parking_space

def main():
    zones_count = int(input())
    zones = []

    for _ in range(zones_count):
        name, params = input().split(': ')
        x, y, length, width, price = map(float if '.' in params else int, params.split(', '))
        zones.append(Zone(name, x, y, length, width, price))

    parking_spaces = []
    for space in input().split('; '):
        x, y = map(int, space.split(', '))
        parking_spaces.append((x, y))

    target_x, target_y = map(int, input().split(', '))
    time_constant = int(input())

    min_total_price = float('inf')
    best_parking_space = None
    best_zone_name = ''

    for zone in zones:
        for x, y in parking_spaces:
            if zone.min_x <= x < zone.max_x and zone.min_y <= y < zone.max_y:
                space = ParkingSpace(x, y, target_x, target_y)
                zone.add_parking_space(space)

    for zone in zones:
        current_best = zone.best_parking_space
        if current_best:
            total_distance = current_best.distance_from_target
            total_time_seconds = total_distance * 2 * time_constant
            total_time_minutes = math.ceil(total_time_seconds / 60 * 0.50)
            total_price = total_time_minutes * zone.price_per_min
            if total_price < min_total_price:
                min_total_price = total_price
                best_parking_space = current_best
                best_zone_name = zone.name

    print(f"Zone Type: {best_zone_name}; X: {best_parking_space.x}; Y: {best_parking_space.y}; Price: {min_total_price:.2f}")

if __name__ == "__main__":
    main()
