import src.service as service
import src.find as find
import pyautogui
import time


# предполагается, что настройки графики игры стоят на минимуме (чтобы не было фона)
def main():
    time.sleep(5)
    original = service.take_screenshot()
    image = original.copy()
    compressed_image = image.resize((160, 90))

    pyautogui.click(find.bonus_box_screen_coordinates(compressed_image))


if __name__ == "__main__":
    main()
