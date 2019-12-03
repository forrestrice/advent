def box_distance(s1, s2):
    shortest_length = min(len(s1), len(s2))
    distance = 0
    for idx in range(shortest_length):
        distance += s1[idx] != s2[idx]
    return distance


class BKNode():
    def __init__(self, content):
        self.content = content
        self.leaves_by_distance = {}

    def propagate_child(self, descendent):
        if descendent.content == self.content:
            return
        distance = box_distance(self.content, descendent.content)
        if distance in self.leaves_by_distance:
            self.leaves_by_distance[distance].propagate_child(descendent)
        else:
            self.leaves_by_distance[distance] = descendent

    def find_matching(self, target, tolerance, verbose = False):
        distance = box_distance(self.content, target)
        if verbose:
            print("node={0}, target={1}, distance={2}".format(self.content, target, distance))
        candidates = []
        if  0 < distance <= tolerance:
            candidates.append(self)
        for candidate_distance in range(distance - tolerance, distance + tolerance + 1):
            if candidate_distance in self.leaves_by_distance:
                candidates.extend(self.leaves_by_distance[candidate_distance].find_matching(target, tolerance, verbose))

        if verbose:
            print("returning candidates", candidates)
        return candidates


def build_bk_tree(input_file):
    with open(input_file, "r") as boxes:
        root_node = None
        for box_code in boxes:
            box_node = BKNode(box_code)
            if root_node is None:
                root_node = box_node
            else:
                root_node.propagate_child(box_node)
    return root_node


input_file = "box_input.txt"
bk_tree_root = build_bk_tree(input_file)

winning_boxes = []
with open(input_file, "r") as boxes:
    for box_code in boxes:
        matching_boxes = bk_tree_root.find_matching(box_code, 1)
        if matching_boxes:
            winning_boxes.append(matching_boxes[0].content)

print(winning_boxes[0], winning_boxes[1])
print(''.join([c for idx,c in enumerate(winning_boxes[0]) if c == winning_boxes[1][idx]]))
