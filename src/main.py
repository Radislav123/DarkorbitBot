from src.find import *
from src.coordinates import *
import pyautogui
import time


# предполагается, что настройки графики игры стоят на минимуме (чтобы не было фона)
def main():
    max_coordinates = tuple((200, 150))
    time.sleep(5)
    original = take_screenshot_for_finding()
    image = original.copy()
    compressed_image = image.resize((160, 90))

    pyautogui.click(bonus_box_screen_coordinates(compressed_image))
    current_coordinates = get_current_coordinates()



if __name__ == "__main__":
    main()
