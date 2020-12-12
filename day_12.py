with open('day_12.txt') as p:
    instructions = [(line[0], int(line[1:])) for line in p]

# Part 1
class State:
    def __init__(self, x, y, current_dir):
        self.x = x
        self.y = y
        self._current_dir = current_dir

    @property
    def current_dir(self):
        if self._current_dir == 0:
            return 1, 0
        elif self._current_dir == 90:
            return 0, 1
        elif self._current_dir == 180:
            return -1, 0
        elif self._current_dir == 270:
            return 0, -1

    def change_dir(self, deg_change):
        self._current_dir = (self._current_dir + deg_change) % 360

    def move(self, del_x, del_y):
        self.x, self.y = self.x + del_x, self.y + del_y

    def apply_instruction(self, ins):
        dir, unit = ins
        if dir == 'N':
            self.move(0, unit)
        elif dir == 'S':
            self.move(0, -unit)
        elif dir == 'E':
            self.move(unit, 0)
        elif dir == 'W':
            self.move(-unit, 0)
        elif dir == 'F':
            self.move(unit * self.current_dir[0], unit * self.current_dir[1])
        elif dir == 'L':
            self.change_dir(unit)
        elif dir == 'R':
            self.change_dir(-unit)


state = State(0, 0, 0)

for instruction in instructions:
    state.apply_instruction(instruction)
#     print(state.x, state.y, state._current_dir)
#
# print("Part 1", abs(state.x)+abs(state.y))


# Part 2
class WPState:

    def __init__(self, wp_x, wp_y):
        self.wp_x = wp_x
        self.wp_y = wp_y
        self.ship_x = 0
        self.ship_y = 0

    def rotate_wp(self, deg):
        if deg < 0:
            deg = 360 + deg
        if deg == 90:
            self.wp_x, self.wp_y = -self.wp_y, self.wp_x
        elif deg == 180:
            self.wp_x, self.wp_y = -self.wp_x, -self.wp_y
        elif deg == 270:
            self.wp_x, self.wp_y = self.wp_y, -self.wp_x

    def move_wp(self, del_x, del_y):
        self.wp_x, self.wp_y = self.wp_x + del_x, self.wp_y + del_y

    def move_ship(self, unit):
        self.ship_x, self.ship_y = self.ship_x + unit * self.wp_x, self.ship_y + unit * self.wp_y

    def apply_instruction(self, ins):
        dir, unit = ins
        if dir == 'N':
            self.move_wp(0, unit)
        elif dir == 'S':
            self.move_wp(0, -unit)
        elif dir == 'E':
            self.move_wp(unit, 0)
        elif dir == 'W':
            self.move_wp(-unit, 0)
        elif dir == 'F':
            self.move_ship(unit)
        elif dir == 'L':
            self.rotate_wp(unit)
        elif dir == 'R':
            self.rotate_wp(-unit)


state = WPState(10, 1)

for instruction in instructions:
    state.apply_instruction(instruction)

print("Part 2", abs(state.ship_x) + abs(state.ship_y))

