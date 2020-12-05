with open('day_1.txt') as p:
    numbers: list[int] = list(map(int, p))

# Part 1
for index_i, i in enumerate(numbers):
    for j in numbers[index_i:]:
        if i + j == 2020:
            print("Product of 2 numbers that add up to 2020:", i * j)


# Part 2
for index_i, i in enumerate(numbers):
    for index_j, j in enumerate(numbers[index_i:]):
        for index_k, k in enumerate(numbers[index_i + index_j:]):
            if i + j + k == 2020:
                print("Product of 3 numbers that add up to 2020:", i * j * k)
