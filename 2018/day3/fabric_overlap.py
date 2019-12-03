import re
from collections import defaultdict
from functools import reduce

all_claim_points = defaultdict(list)
point_frequency = defaultdict(int)
with open("fabric_claims.txt", "r") as claims:
    for claim in claims:
        match = re.search('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', claim)
        id, w_offset, h_offset, width, height = int(match.group(1)), int(match.group(2)), \
                                                int(match.group(3)), int(match.group(4)), int(match.group(5))
        w_start = w_offset + 1
        h_start = h_offset + 1
        for col in range(w_start, w_start + width):
            for row in range(h_start, h_start + height):
                point = (col, row)
                point_frequency[point] = point_frequency[point] + 1
                all_claim_points[id].append(point)

overlap = [point for point in point_frequency if point_frequency[point] > 1]
print(len(overlap))  # solution 1

for claim, claim_points in all_claim_points.items():
    point_sole_owner_flags = list(map(lambda point: point_frequency[point] == 1, claim_points))
    area_sole_owner = reduce(lambda x, y: x and y, point_sole_owner_flags)
    if area_sole_owner:
        print(claim)  # solution 2
