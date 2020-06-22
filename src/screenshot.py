from PIL import ImageGrab, ImageDraw


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
