from navigate import *
from service import *
from main import *
import pyautogui
import glob


def fun_0():
    time.sleep(4)
    pyautogui.click(get_screen_coordinates(119, 64))
    time.sleep(25)
    main(10*60, 100)


def fun_1():
    map_size = [210, 130]
    for i in range(10):
        current_coordinates = [random.randint(0, 10), random.randint(0, 10)]
        x_offset = 0
        y_offset = 0

        x_offset, y_offset = add_offset_by_center(x_offset, y_offset, current_coordinates, map_size)
        x_offset, y_offset = add_offset_by_fourth(x_offset, y_offset, current_coordinates, map_size)
        new_coordinates = get_new_place_screen_coordinates(current_coordinates, map_size)
        print("current_coordinates : " + str(current_coordinates))
        print("x offset : " + str(x_offset))
        print("y offset : " + str(y_offset))
        print("new coordinates : " + str(get_coordinates_from_screen_coordinates(new_coordinates)))
        print("is coordinates valid : " + str(check_coordinates_to_fly(map_size, get_coordinates_from_screen_coordinates(new_coordinates))))
        print()

    for i in range(10):
        current_coordinates = [map_size[0] + random.randint(0, 10), map_size[1] + random.randint(0, 10)]
        x_offset = 0
        y_offset = 0

        x_offset, y_offset = add_offset_by_center(x_offset, y_offset, current_coordinates, map_size)
        x_offset, y_offset = add_offset_by_fourth(x_offset, y_offset, current_coordinates, map_size)
        new_coordinates = get_new_place_screen_coordinates(current_coordinates, map_size)
        print("current_coordinates : " + str(current_coordinates))
        print("x offset : " + str(x_offset))
        print("y offset : " + str(y_offset))
        print("new coordinates : " + str(get_coordinates_from_screen_coordinates(new_coordinates)))
        print("is coordinates valid : " + str(check_coordinates_to_fly(map_size, get_coordinates_from_screen_coordinates(new_coordinates))))
        print()


def fun_2():
    time.sleep(4)
    main(0, 20)


fun_2()
