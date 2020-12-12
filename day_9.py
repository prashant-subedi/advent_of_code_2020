with open('day_9.txt') as p:
    numbers = [int(line.strip()) for line in p]

preamble_size = 25

# Part 1
def sum_of_any_two(array, num):
    for i, num_1 in enumerate(array):
        for num_2 in array[i:]:
            if num_1 + num_2 == num:
                return True
    return False


for index, number in enumerate(numbers[preamble_size:]):
    if not sum_of_any_two(numbers[index: index + preamble_size], number):
        print("Part 1 solution", number)
        break

# Part 2
sum_number_index = index
sum_number = number
# A 2 D array represented by index, offset
# index is the starting
# calc_memory[a][b] -> sum of numbers form index b to next a numbers
# initializing with a[0][x] representing the number it self
calc_memory = {
    0: {i: number for i, number in enumerate(numbers) if i < sum_number_index}
}
offset = 1
max_index = len(calc_memory[0])
calc_memory[0][max_index] = numbers[max_index]
while offset < max_index:
    calc_memory[offset] = {}
    for i in range(max_index):
        if i + offset > max_index:
            break
        calc_memory[offset][i] = calc_memory[offset - 1][i] + calc_memory[0][i + offset]
        if calc_memory[offset][i] == sum_number:
            smallest, *rest, largest = sorted(numbers[i: i + offset + 1])
            print("Part 2 solution", smallest + largest )
            exit()
    offset += 1
