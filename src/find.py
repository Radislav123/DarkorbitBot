import src.logger as log


def bonus_box_resized_image_coordinates(compressed_image):
    image_pixels = compressed_image.load()
    for x in range(compressed_image.size[0]):
        for y in range(compressed_image.size[1]):
            if 230 < image_pixels[x, y][0] < 256\
                    and 230 < image_pixels[x, y][1] < 256\
                    and 230 < image_pixels[x, y][2] < 256:
                return x, y
    return -1, -1


def bonus_box_image_coordinates(compressed_image):
    x, y = bonus_box_resized_image_coordinates(compressed_image)
    if (x, y) != (-1, -1):
        # добавляется смещение из-за погрешностей, возникающих при сжатии
        x = x*10 + 5
        y = y*10 + 5
    return x, y


def bonus_box_screen_coordinates(compressed_image):
    x, y = bonus_box_image_coordinates(compressed_image)
    if (x, y) != (-1, -1):
        y += 100
    return x, y
