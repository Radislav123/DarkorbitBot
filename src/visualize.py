from src.service import to_sources
import src.find as find


def save_found_box(image, resized_image):
    image_coordinates = find.bonus_box_resized_image_coordinates(resized_image)
    screen_coordinates = find.bonus_box_image_coordinates(resized_image)

    inner_image = image.copy()
    inner_resized_image = resized_image.copy()

    # перекрашивается в красный точка с координатами коробки
    loaded = inner_resized_image.load()
    x, y = image_coordinates
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            loaded[i, j] = (255, 0, 0)

    # то же самое, что выше, только для несжатого изображения, и точек теперь побольше
    loaded = inner_image.load()
    x, y = screen_coordinates
    for i in range(x - 10, x + 11):
        for j in range(y - 10, y + 11):
            loaded[i, j] = (255, 0, 0)

    inner_image.save(to_sources("found\\bonus_box.png"))
    inner_resized_image.save(to_sources("found\\bonus_box_compressed.png"))
