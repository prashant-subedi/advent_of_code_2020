with open('day_10.txt') as p:
    adapters = [int(line.strip()) for line in p]

sorted_adapters = sorted(adapters)
sorted_adapters = [0] + sorted_adapters + [sorted_adapters[-1] + 3]

# Part 1
from collections import Counter

diffs = []
for prev, current in zip(sorted_adapters, sorted_adapters[1:]):
    diffs.append(current - prev)

diff_counter = Counter(diffs)
print("Part 1:", diff_counter[1] * diff_counter[3])


# Part 2
from collections import defaultdict


def find_total_paths(adapter_sequence):
    paths = defaultdict(int, {0: 1})
    for index, adapter in enumerate(adapter_sequence):
        for prev_adapter in reversed(adapter_sequence[:index]):
            if adapter - prev_adapter <= 3:
                paths[adapter] += paths[prev_adapter]
            else:
                break
    return paths[adapter_sequence[-1]]


print("Part 2:", find_total_paths(sorted_adapters))