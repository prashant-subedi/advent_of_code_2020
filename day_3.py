from functools import reduce
import operator


class LocalGeology:
    def __init__(self, slope):
        with open('day_3.txt') as p:
            self._tree_pattern: list[str] = list(p)

        self._slope_x, self._slope_y = slope

        self._width = len(self._tree_pattern[0][:-1])

        self._height = len(self._tree_pattern)

        self._current_x, self._current_y = (0, 0)

    def __iter__(self):
        while True:
            self._current_x = self._current_x + self._slope_x
            self._current_y = self._current_y + self._slope_y

            if self._current_y >= self._height:
                return
            yield self._tree_pattern[self._current_y][self._current_x % self._width]


def find_trees_in_path(slope):
    count = 0
    for i in LocalGeology(slope):
        if i == "#":
            count += 1
    return count


def trees_for_slopes(slopes):
    trees = []
    for slope in slopes:
        trees.append(find_trees_in_path(slope))
    return trees


print("Part 1 solution", find_trees_in_path((3, 1)))

print(
    "Part 2 solution",
    reduce(operator.mul, trees_for_slopes([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
)
