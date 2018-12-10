from collections import defaultdict

# all_slot_frequencies = defaultdict(lambda: defaultdict(lambda: 0))
min_x, min_y, max_x, max_y = None, None, None, None
starting_points = set()
with open("taxi_input_example.txt", "r") as points_file:
    for point_str in points_file:
        split_list = point_str.split(",")
        x, y = int(split_list[0]), int(split_list[1])
        starting_points.add((x, y))
        if min_x is None or x < min_x:
            min_x = x
        if min_y is None or y < min_y:
            min_y = y
        if max_x is None or x > max_x:
            max_x = x
        if max_y is None or y > max_y:
            max_y = y

unclaimed_points = {}  # defaultdict(list)
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        point = (x, y)
        if point not in starting_points:
            unclaimed_points[point] = []
        #print(point, len(unclaimed_points))
print("starting with {} unclaimed points".format(len(unclaimed_points)))
print("starting with {} starting points".format(len(starting_points)))

def legal_neighbors(point):
    neighbors = []
    x, y = point[0], point[1]
    if x > min_x:
        neighbors.append((x - 1, y))
    if x < max_x:
        neighbors.append((x + 1, y))
    if y > min_y:
        neighbors.append((x, y - 1))
    if y < max_y:
        neighbors.append((x, y + 1))
    #if len(neighbors) < 4:
        #print(point, neighbors)
    return neighbors

frontier = set(starting_points)
claim_by_point = defaultdict(list)
while frontier:
    #print(len(frontier))
    print("\n\n")
    print(sorted(frontier))
    print(len(claim_by_point))

    potential_frontier = set()
    new_frontier = set()
    for frontier_point in frontier:
        for neighbor in legal_neighbors(frontier_point):
            if neighbor in unclaimed_points:
                unclaimed_points[neighbor].append(frontier_point)
                potential_frontier.add(neighbor)
    for candidate_point in potential_frontier:
        point_claimants =  unclaimed_points[candidate_point]
        if len(point_claimants) == 1:
            new_frontier.add(candidate_point)
            claim_by_point[point_claimants[0]].append(candidate_point)
        unclaimed_points.pop(candidate_point)
    frontier = new_frontier

def enumerate_claim(point):
    to_process = [point]
    claim = []
    while(to_process):
        current_point = to_process.pop()
        new_claim_points = claim_by_point[current_point]
        claim.append(current_point)
        to_process.extend(new_claim_points)
    return claim

max_claim_size = -1
claim_sum = 0
for point in starting_points:
    point_claim_size = len(enumerate_claim(point))
    print(point,  sorted(enumerate_claim(point)))
    claim_sum += point_claim_size
    if point_claim_size > max_claim_size and len(legal_neighbors(point)) == 4:
        max_claim_size = point_claim_size

print("answer: ", max_claim_size)
print("claim_sum:", claim_sum)
print("area_points:", (max_x + 1 - min_x) * (max_y + 1 - min_y))


