from src.service import *
from PIL import Image


# делает скриншот номера карты и координат
def take_coordinates_and_map_screenshot():
    return take_screenshot((1642, 842, 1760, 852))


def crop_map_from_coordinates_image(image):
    return image.crop((0, 0, 19, image.size[1]))


def crop_coordinates_from_coordinates_and_map_image(image):
    return image.crop((24, 0, image.size[0], 10))


# 2х2 image
def get_gray_number(image):
    return [
        sum(number_colors(image, 0, 0))//3,
        sum(number_colors(image, 0, 1))//3,
        sum(number_colors(image, 1, 0))//3,
        sum(number_colors(image, 1, 1))//3
    ]


def get_numbers():
    array = []
    for i in range(10):
        image = Image.open(from_navigate(str(i) + ".png")).resize((2, 2))
        array.append(get_gray_number(image))
    return array


# number_image - то, что сравнивается/прговеряется
# model_number - число-стандарт, то, с чем сравнивается
def assert_number(number_image, model_number):
    compressed_number_image = number_image.resize((2, 2))
    gray_number = get_gray_number(compressed_number_image)
    bound = 10
    result = (model_number[0] - bound < gray_number[0] < model_number[0] + bound)\
             and (model_number[1] - bound < gray_number[1] < model_number[1] + bound) \
             and (model_number[2] - bound < gray_number[2] < model_number[2] + bound) \
             and (model_number[3] - bound < gray_number[3] < model_number[3] + bound)
    return result


def get_number(number_image, numbers):
    for i in range(10):
        if assert_number(number_image, numbers[i]):
            return i
    return -1


def is_slash(image):
    slash_image = Image.open(from_navigate("slash.png")).resize((2, 2))
    gray_slash = get_gray_number(slash_image)
    return assert_number(image, gray_slash)


def is_blank(image):
    blank_image = Image.open(from_navigate("blank.png")).resize((2, 2))
    gray_blank = get_gray_number(blank_image)
    return assert_number(image, gray_blank)


# x, y == [0, 1]
def number_colors(number: Image, x, y):
    return number.load()[x, y][0:3]


def get_x(image, numbers):
    previous_position = 0
    next_position = 8
    x = ""
    while True:
        number_image = image.crop((previous_position, 0, next_position, image.size[1]))
        number = get_number(number_image, numbers)
        if number == -1:
            next_position -= 1
            previous_position -= 1
            if is_slash(number_image):
                break
        else:
            next_position += 8
            previous_position += 8
            x += str(number)
    return int(x), next_position


def get_y(image, numbers, y_start_position):
    previous_position = y_start_position
    next_position = previous_position + 8
    y = ""
    while True:
        number_image = image.crop((previous_position, 0, next_position, image.size[1]))
        number = get_number(number_image, numbers)
        if number == -1:
            next_position -= 1
            previous_position -= 1
            if is_blank(number_image):
                break
        else:
            next_position += 8
            previous_position += 8
            y += str(number)
    return int(y)


def get_current_coordinates():
    numbers = get_numbers()
    coordinates_image = crop_coordinates_from_coordinates_and_map_image(take_coordinates_and_map_screenshot())
    # y_start_position чтобы избежать попытки распознать слэш как начало y
    x, y_start_position = get_x(coordinates_image, numbers)
    y = get_y(coordinates_image, numbers, y_start_position)
    return x, y
