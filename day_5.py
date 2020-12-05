with open('day_5.txt') as p:
    passes: list[str] = list(i.strip() for i in p)


def find_seat_id(seat_str: str) -> dict[str: tuple[int, int]]:
    partition = 64
    row_id = 0
    col_id = 0
    for row_str in seat_str[:7]:
        if row_str == 'B':
            row_id += partition
        partition /= 2

    partition = 4
    for col_str in seat_str[7:]:
        if col_str == 'R':
            col_id += partition
        partition /= 2
    return int(row_id * 8 + col_id)


taken_seat_ids = [find_seat_id(i) for i in passes]

# Part 1
print("Part 1 solution", max(taken_seat_ids))

# Part 2
for i in range(1, 1024):# Skip the first and last seats
    if i not in taken_seat_ids:
        if i - 1 in taken_seat_ids and i + 1 in taken_seat_ids:
            print("Part 2", i)