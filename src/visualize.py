from service import *
import find
import glob
import os


def get_saved_bonus_boxes_images_names():
    return glob.glob(to_found("*bonus_box*.png"))


def get_saved_bonus_boxes_number():
    return len(get_saved_bonus_boxes_images_names())//4


# formatted_time = time.strftime("%x_%X")
def save_found_box_images(image, compressed_image, formatted_time, max_saves = 20):
    image_coordinates = find.bonus_box_resized_image_coordinates(compressed_image)
    screen_coordinates = find.bonus_box_image_coordinates(compressed_image)

    inner_image = image.copy()
    inner_compressed_image = compressed_image.copy()

    # перекрашивается в красный точка с координатами коробки
    loaded = inner_compressed_image.load()
    x, y = image_coordinates
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i < 160 and 0 <= j < 90:
                loaded[i, j] = (255, 0, 0)

    # то же самое, что выше, только для несжатого изображения, и точек теперь побольше
    loaded = inner_image.load()
    x, y = screen_coordinates
    for i in range(x - 10, x + 11):
        for j in range(y - 10, y + 11):
            if 0 <= i < 1600 and 0 <= j < 900:
                loaded[i, j] = (255, 0, 0)

    # связать с логом через названия или еще один лог
    if get_saved_bonus_boxes_number() >= max_saves:
        for file_name in get_saved_bonus_boxes_images_names()[0:4]:
            os.remove(file_name)

    image.save(to_found(formatted_time + "_bonus_box.png"))
    compressed_image.save(to_found(formatted_time + "_bonus_box_compressed.png"))
    inner_image.save(to_found(formatted_time + "_bonus_box_marked.png"))
    inner_compressed_image.save(to_found(formatted_time + "_bonus_box_compressed_marked.png"))

