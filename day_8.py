with open('day_8.txt') as p:
    instructions = [line.split() for line in p]


def process(instructions) -> (int, bool):
    current_instruction = 0
    visited_instructions = set()
    accumulator_value = 0

    while current_instruction < len(instructions):
        op, arg = instructions[current_instruction]
        next_instruction = current_instruction + 1
        visited_instructions.add(current_instruction)
        if op == "nop":
            pass
        elif op == "acc":
            accumulator_value += int(arg)
        elif op == "jmp":
            next_instruction = current_instruction + int(arg)

        if next_instruction in visited_instructions:
            return accumulator_value, True

        current_instruction = next_instruction
    return accumulator_value, False


# Part 1
print("Part 1 solution", process(instructions)[0])

# Part 2
for index, instruction in enumerate(instructions):
    op, arg = instruction
    if op == "acc":
        continue

    old_ins = instructions[index]
    if op == "jmp":
        instructions[index] = ("nop", arg)
    elif op == "nop":
        instructions[index] = ("jmp", arg)

    acc_value, looped = process(instructions)

    instructions[index] = old_ins

    if not looped:
        print("Part 2 solution", acc_value)
        break

