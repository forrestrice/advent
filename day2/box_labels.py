from collections import defaultdict

all_slot_frequencies = defaultdict(lambda: defaultdict(lambda: 0))
with open("box_input.txt", "r") as boxes:
    for box_code in boxes:
        for idx, char in enumerate(box_code):
            all_slot_frequencies[idx][char] = all_slot_frequencies[idx][char] + 1
    print(all_slot_frequencies)
    boxes.seek(0)
    right_boxes = []
    for box_code in boxes:
        slot_twins = 0
        for idx, char in enumerate(box_code):
            slot_twins += all_slot_frequencies[idx][char] > 1
        if slot_twins == len(box_code) - 1:
            print(box_code)
            right_boxes.append(box_code)
    print([c for c in right_boxes[0] if c in right_boxes[1]])