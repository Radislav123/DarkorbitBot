from PIL import Image, ImageGrab, ImageDraw
import time


def to_sources(path: str):
    return from_sources(path)


def from_sources(path: str):
    return "..\\resources\\" + path


def print_time(function, *args, **kwargs):
    start = time.time()
    value = function(*args, **kwargs)
    end = time.time()
    print(function.__name__ + " : " + str(end - start))
    return value


def print_attributes(obj):
    for name, value in obj.__dict__.items():
        print(name + " : " + str(value))


def close_spaceship(image):
    ImageDraw.Draw(image).rectangle([870, 300, 1070, 540], fill = "black")


def take_screenshot():
    # соотношение сторон скриншота 16x9, так как это принудительно устанавливаемое соотношение при сжатии
    # ну, и сжимать пропорционально проще
    image = ImageGrab.grab(bbox = (0, 100, 1600, 1000))
    close_spaceship(image)
    return image
