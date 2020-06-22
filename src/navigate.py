import random

# 0 | 1
# - + -
# 2 | 3
from collections import Iterable


def get_fourth(coordinates, map_size):
    fourth = 0

    if coordinates[0] > map_size[0]//2:
        fourth += 1
    if coordinates[1] > map_size[1]//2:
        fourth += 2

    return fourth


def add_offset_by_fourth(x, y, coordinates, map_size):
    fourth = get_fourth(coordinates, map_size)
    offset_by_fourth = 10
    x_offset = 0
    y_offset = 0

    if fourth == 0:
        x_offset = offset_by_fourth
    elif fourth == 1:
        y_offset = offset_by_fourth
    elif fourth == 2:
        y_offset = -offset_by_fourth
    else:
        x_offset = -offset_by_fourth

    return x + x_offset, y + y_offset


def add_offset_by_center(x, y, coordinates, map_size):
    offset_reducing_reducing = 20
    x_offset_reducing = map_size[0]//offset_reducing_reducing
    y_offset_reducing = map_size[1]//offset_reducing_reducing

    if coordinates[0] > map_size[0]//2:
        x_offset = -(map_size[0]//4*3 - coordinates[0])//x_offset_reducing
    else:
        x_offset = (map_size[0]//4*1 - coordinates[0])//x_offset_reducing

    if coordinates[1] > map_size[1]//2:
        y_offset = -(map_size[1]//4*3 - coordinates[1])//y_offset_reducing
    else:
        y_offset = (map_size[1]//4*1 - coordinates[1])//y_offset_reducing

    return x + x_offset, y + y_offset


def get_screen_coordinates(x, y):
    return x + 1693, y + 889


def get_coordinates_from_screen_coordinates(x, y = 0):
    if isinstance(x, Iterable):
        return x[0] - 1693, x[1] - 889
    return x - 1693, y - 889


def check_coordinates_to_fly(map_size, x, y = 0):
    if isinstance(x, Iterable):
        y = x[1]
        x = x[0]
    safe_bound = 10
    return (safe_bound < x < map_size[0] - safe_bound) and (safe_bound < y < map_size[1] - safe_bound)


def get_new_place_screen_coordinates(current_coordinates, map_size):
    random_bound = 6
    x_offset = 0
    y_offset = 0
    x = -1
    y = -1

    x_offset, y_offset = add_offset_by_center(x_offset, y_offset, current_coordinates, map_size)
    x_offset, y_offset = add_offset_by_fourth(x_offset, y_offset, current_coordinates, map_size)

    while not check_coordinates_to_fly(map_size, x, y):
        x = current_coordinates[0] + x_offset + random.randint(-random_bound, random_bound)
        y = current_coordinates[1] + y_offset + random.randint(-random_bound, random_bound)

    return get_screen_coordinates(x, y)


def get_safe_zone_screen_coordinates():
    return get_screen_coordinates(185, 20)
