from src.coordinates import *
from src.navigate import *
from src.find import *
import pyautogui
import time


# размер миникарты должен быть на 1 больше минимального
# предполагается, что настройки графики игры стоят на минимуме (чтобы не было фона)
def main():
    map_size = tuple((200, 130))
    time.sleep(5)
    bonus_boxes = 0

    while bonus_boxes < 3:
        image = take_screenshot_for_finding()
        compressed_image = image.resize((160, 90))

        click_coordinates = bonus_box_screen_coordinates(compressed_image)
        if click_coordinates == (-1, -1):
            click_coordinates = find_new_place(get_current_coordinates(), map_size)
            pyautogui.click(click_coordinates)
            time.sleep(6)
        else:
            pyautogui.click(click_coordinates)
            bonus_boxes += 1
            time.sleep(3)


if __name__ == "__main__":
    main()
