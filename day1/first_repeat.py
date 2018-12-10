input_file_name = "time_machine_input.txt"

def infinite_input():
    input_file = open(input_file_name, "r")
    while True:
        for line in input_file:
            yield line
        input_file.seek(0)

sum = 0
seen_sums = {}
for time_input in infinite_input():
    sum += int(time_input)
    sum_frequency = seen_sums.get(sum, 0) + 1
    seen_sums[sum] = sum_frequency
    if sum_frequency > 1:
        print(sum)
        break