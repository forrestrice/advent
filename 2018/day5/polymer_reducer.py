import string
import time

with open("polymer_input.txt", "r") as polymer_input:
    polymer = polymer_input.readline()


def good_polymer_length(poly):
    processed = []

    for c in poly:
        if not processed:
            processed.append(c)
        elif c.lower() == processed[-1].lower() and c != processed[-1]:
            processed.pop()
        else:
            processed.append(c)
    return len(processed)


def polymer_length(poly):
    while True:
        length = len(poly)
        new_polymer = []
        index = 0
        pairs_removed = 0
        while index < length - 1:
            index_c = poly[index]
            next_c = poly[index + 1]
            if index_c.lower() == next_c.lower() and index_c != next_c:
                # print("removing {}, {} at indicies {}, {}".format(index_c, next_c, index, index + 1))
                index += 1
                pairs_removed += 1
                if index == length - 2:
                    new_polymer.append(poly[-1])
            else:
                new_polymer.append(index_c)
                if index == length - 2:
                    new_polymer.append(next_c)
            index += 1
        # print(len(new_polymer), len(new_polymer) + pairs_removed * 2, length, polymer[0], new_polymer[0], polymer[-5:],
        # new_polymer[-5:])
        poly = new_polymer

        if (len(poly) == length):
            break
    return length


t0 = time.time()
reduced_size = {}
for c in string.ascii_lowercase:
    reduced_polymer = polymer.replace(c, '').replace(c.upper(), '')
    reduced_size[c] = polymer_length(reduced_polymer)
    print(c, reduced_size[c])

print(min(reduced_size, key=reduced_size.get))
t1 = time.time()
reduced_size = {}
for c in string.ascii_lowercase:
    reduced_polymer = polymer.replace(c, '').replace(c.upper(), '')
    reduced_size[c] = good_polymer_length(reduced_polymer)
    print(c, reduced_size[c])

print(min(reduced_size, key=reduced_size.get))
t2 = time.time()

print("bad hack {} seconds".format( t1 - t0))
print("good clean living {} seconds".format( t2 - t1))
