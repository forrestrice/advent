from typing import Tuple


def up(point: Tuple[int, int]) -> Tuple[int, int]:
    return point[0], point[1] + 1


def down(point: Tuple[int, int]) -> Tuple[int, int]:
    return point[0], point[1] - 1


def left(point: Tuple[int, int]) -> Tuple[int, int]:
    return point[0] - 1, point[1]


def right(point: Tuple[int, int]) -> Tuple[int, int]:
    return point[0] + 1, point[1]


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def dist_from_origin(p):
    return manhattan_distance(p, (0, 0))


direction_dict = {'U': up, 'D': down, 'L': left, 'R': right}


class Wire:
    def __init__(self, wire_paths):
        self.point_steps = {}
        self.steps = 0
        current_point = (0, 0)
        for wire_path in wire_paths:
            current_point = self.__add_points(current_point, wire_path)

    def __add_points(self, current_point, wire_path):
        direction = wire_path[0]
        direction_function = direction_dict[direction]
        magnitude = int(wire_path[1:])
        for i in range(0, magnitude):
            current_point = direction_function(current_point)
            self.steps += 1
            if current_point not in self.point_steps:
                self.point_steps[current_point] = self.steps
        return current_point


with open("wire_input.txt", "r") as wires:
    wire1 = Wire(wires.readline().split(","))
    wire2 = Wire(wires.readline().split(","))

intersection = wire1.point_steps.keys() & wire2.point_steps.keys()
sorted_intersection = sorted(intersection, key=dist_from_origin)
print("solution 1: {}".format(sorted_intersection[0]))

time_sorted = sorted(intersection, key=lambda p: wire1.point_steps[p] + wire2.point_steps[p])
part2_answer = wire1.point_steps[time_sorted[0]] + wire2.point_steps[time_sorted[0]]
print("solution 2: {}".format(part2_answer))
