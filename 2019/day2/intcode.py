with open("computer_input.txt", "r") as copmuter_input:
    instructions = [int(x) for x in copmuter_input.readline().split(",")]

print(instructions)


def run(program, counter=0):
    instruction = program[counter]
    if instruction == 99:
        return
    elif instruction == 1:
        output_value = program[program[counter + 1]] + program[program[counter + 2]]
    else:
        output_value = program[program[counter + 1]] * program[program[counter + 2]]
    program[program[counter + 3]] = output_value
    return run(program, counter + 4)


def run_with_inputs(program, noun, verb):
    program_copy = program[:]
    program_copy[1] = noun
    program_copy[2] = verb
    run(program_copy)
    return program_copy


part1_result = run_with_inputs(instructions, 12, 2)
print("solution 1: {}".format(part1_result[0]))

# for/else calls else block if loop isn't broken
for n in range(0, 100):
    for v in range(0, 100):
        result = run_with_inputs(instructions, n, v)
        if result[0] == 19690720:
            print(n, v)
            print("solution 2: {}".format(100 * n + v))
            break
    else:
        continue
    break
