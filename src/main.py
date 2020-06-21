from src.coordinates import *
from src.navigate import *
from src.find import *
import pyautogui
import time


# размер миникарты должен быть на 1 больше минимального
# предполагается, что настройки графики игры стоят на минимуме (чтобы не было фона)
def main():
    map_size = tuple((200, 130))
    time.sleep(3)
    bonus_boxes = 0
    fly_time = 6
    collect_time = 3
    start_time = time.time()

    # while bonus_boxes < 100:
    while time.time() - start_time < 60*1:
        image = take_screenshot_for_finding()
        compressed_image = image.resize((160, 90))

        click_coordinates = bonus_box_screen_coordinates(compressed_image)
        if click_coordinates == (-1, -1):
            click_coordinates = find_new_place(get_current_coordinates(), map_size)
            pyautogui.click(click_coordinates)
            time.sleep(fly_time)
        else:
            pyautogui.click(click_coordinates)
            bonus_boxes += 1
            time.sleep(collect_time)
    else:
        pyautogui.click(find_safe_zone())

    print("final")
    print("bonus boxes" + " : " + str(bonus_boxes))


if __name__ == "__main__":
    main()
