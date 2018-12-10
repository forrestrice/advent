def box_histogram(box_code):
    hist = {}
    for c in box_code:
        hist[c] = hist.get(c, 0) + 1
    return hist


contains_double_count = 0
contains_triple_count = 0

with open("box_input.txt", "r") as boxes:
    for box_code in boxes:
        frequencies = box_histogram(box_code).values()
        if 2 in frequencies:
            contains_double_count += 1
        if 3 in frequencies:
            contains_triple_count += 1

print(contains_double_count, contains_triple_count, contains_double_count * contains_triple_count)
