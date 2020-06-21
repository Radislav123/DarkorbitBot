import random


# 0 | 1
# - + -
# 2 | 3
def get_fourth(coordinates, map_size):
    fourth = 0
    if coordinates[0] > map_size[0]//2:
        fourth += 1
    if coordinates[1] > map_size[1]//2:
        fourth += 2
    return fourth


def get_screen_coordinates(x, y):
    return x + 1693, y + 889


def find_new_place(current_coordinates, map_size):
    x = -1
    y = -1
    bound = 20
    while (not 10 < x < map_size[0] - 10) and (not 10 < y < map_size[1] - 10):
        x = random.randint(current_coordinates[0] - bound, current_coordinates[0] + 10)
        y = random.randint(current_coordinates[1] - bound, current_coordinates[1] + 10)
    fourth = get_fourth(current_coordinates, map_size)
    if fourth == 0:
        x += 10
    elif fourth == 1:
        y += 10
    elif fourth == 2:
        y -= 10
    else:
        x -= 10
    return get_screen_coordinates(x, y)


def find_safe_zone():
    return get_screen_coordinates(185, 20)
