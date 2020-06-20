from PIL import ImageGrab, ImageDraw
import time


def from_resources(filename: str):
    return "..\\resources\\" + filename


def to_resources(filename: str):
    return from_resources(filename)


def from_navigate(filename: str):
    return "..\\resources\\navigate\\" + filename


def to_navigate(filename: str):
    return from_navigate(filename)


def print_time(function, *args, **kwargs):
    start = time.time()
    value = function(*args, **kwargs)
    end = time.time()
    print(function.__name__ + " : " + str(end - start))
    return value


def print_attributes(obj):
    for name, value in obj.__dict__.items():
        print(name + " : " + str(value))


def take_screenshot(bbox):
    return ImageGrab.grab(bbox = bbox)


def take_screenshot_for_finding():
    # соотношение сторон скриншота 16x9, так как это принудительно устанавливаемое соотношение при сжатии
    # ну, и сжимать пропорционально проще
    image = take_screenshot(bbox = (0, 100, 1600, 1000))
    close_spaceship(image)
    return image


def close_spaceship(image):
    ImageDraw.Draw(image).rectangle([870, 300, 1070, 540], fill = "black")
