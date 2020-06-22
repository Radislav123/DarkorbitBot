from read_coordinates import *
from screenshot import *
from visualize import *
from navigate import *
from logger import *
from find import *

import pyautogui
import time
import sys


# размер миникарты должен быть на 1 больше минимального
# предполагается, что настройки графики игры стоят на минимуме (чтобы не было фона)
def main(collect_time, max_bonus_boxes):
    execution_time, bonus_boxes = get_execution_time(collect_wrapper, collect_time, max_bonus_boxes)
    log_collected("bonus boxes : " + str(bonus_boxes) + " : collect time : " + str(execution_time))


def collect_wrapper(collect_time, max_bonus_boxes):
    map_size = tuple((210, 130))
    start_time = time.time()
    bonus_boxes = 0
    if collect_time and max_bonus_boxes:
        while time.time() - start_time < collect_time and bonus_boxes < max_bonus_boxes:
            bonus_boxes += collect(map_size)
    elif collect_time:
        while time.time() - start_time < collect_time:
            bonus_boxes += collect(map_size)
    elif max_bonus_boxes:
        while bonus_boxes < max_bonus_boxes:
            bonus_boxes += collect(map_size)

    pyautogui.click(get_safe_zone_screen_coordinates())
    return bonus_boxes


def collect(map_size):
    image = take_screenshot_for_finding()
    compressed_image = image.resize((160, 90))
    box_collected = False
    collect_time = 4
    fly_time = 6

    click_coordinates = bonus_box_screen_coordinates(compressed_image)
    if click_coordinates == (-1, -1):
        click_coordinates = get_new_place_screen_coordinates(get_current_coordinates(), map_size)
        log_debug("current coordinates : " + str(get_current_coordinates()))
        log_debug("coordinates to fly : " + str(get_coordinates_from_screen_coordinates(click_coordinates[0], click_coordinates[1])))
        pyautogui.click(click_coordinates)
        time.sleep(fly_time)
    else:
        pyautogui.click(click_coordinates)
        time.sleep(collect_time)
        box_collected = True
        log_collected("bonus box at : " + str(get_current_coordinates()))
        formatted_time = time.strftime("date_%Y_%m_%d_time_%H_%M_%S")
        save_found_box_images(image, compressed_image, formatted_time)

    return box_collected


# первый аргумент (sys.argv[1]) задает лимит по времени сбора в минутах
# второй аргумент (sys.argv[2]) задает лимит по сбору коробок
# "-1" означает, что аргумент не задан
# если аргументы не заданы вовсе, сбор идет на протяжении 30 минут
# sys.argv[0] == main.py
# ...src>python main.py
# запустит искать коробки на 30 минут
# ...src>python main.py 3
# запустит искать коробки на 3 минуты
# ...src>python main.py -1 10
# запустит искать 10 коробок
# ...src>python main.py 3 10
# запустит искать 10 коробок на 3 минуты
if __name__ == "__main__":
    collect_time_main = 0
    max_bonus_boxes_main = 0
    if len(sys.argv) == 1:
        collect_time_main = 60*30
    elif len(sys.argv) == 2:
        collect_time_main = 60*int(sys.argv[1])
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-1":
            max_bonus_boxes_main = int(sys.argv[2])
        else:
            collect_time_main = 60*int(sys.argv[1])
            max_bonus_boxes_main = int(sys.argv[2])
    else:
        print("Что-то пошло не так при распознании аргументов")
        exit(1)
    # ожидание, чтобы открыть окно игры вручную
    time.sleep(4)
    main(collect_time_main, max_bonus_boxes_main)
