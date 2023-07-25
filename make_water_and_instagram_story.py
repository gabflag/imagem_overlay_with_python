from PIL import Image


def resize_background(background_path, new_width):
    background = Image.open(background_path)
    width_percent = (new_width / float(background.size[0]))
    new_height = int((float(background.size[1]) * float(width_percent)))
    resized_background = background.resize((new_width, new_height), Image.LANCZOS)

    return resized_background


def overlay_image_default(background_path, overlay_path, output_path):
    background = resize_background(background_path, 1080)

    overlay = Image.open(overlay_path)

    x = (background.width - overlay.width) // 2
    y = 0

    new_image = Image.new("RGBA", background.size, (0, 0, 0, 0))

    new_image.paste(background, (0, 0))
    new_image.paste(overlay, (x, y), overlay)
    new_image.save(output_path)


def resize_and_overlay_story(
        background_path, overlay_path, output_path):
    
    background = Image.open(background_path)
    overlay = Image.open(overlay_path)
    target_width = 1620
    width_percent = (target_width / float(overlay.width))
    target_height = int((float(overlay.height) * float(width_percent)))
    overlay = overlay.resize((target_width, target_height), Image.LANCZOS)

    if (
        overlay.mode in ('RGBA', 'LA') or
        (overlay.mode == 'P' and 'transparency' in overlay.info)
    ):
        overlay = overlay.convert('RGB')

    x = (background.width - overlay.width) // 2
    y = (background.height - overlay.height) // 2

    new_image = Image.new("RGB", background.size)

    new_image.paste(background, (0, 0))
    new_image.paste(overlay, (x, y))

    new_image.save(output_path, format='JPEG')


def resize_and_overlay_story_vertical(
        background_path, overlay_path, output_path):
    # Abre as imagens usando a biblioteca Pillow
    background = Image.open(background_path)
    overlay = Image.open(overlay_path)

    target_width = 1080
    width_percent = (target_width / float(overlay.width))
    target_height = int((float(overlay.height) * float(width_percent)))
    overlay = overlay.resize((target_width, target_height), Image.LANCZOS)

    if (
        overlay.mode in ('RGBA', 'LA') or
        (overlay.mode == 'P' and 'transparency' in overlay.info)
    ):
        overlay = overlay.convert('RGB')

    x = (background.width - overlay.width) // 2
    y = (background.height - overlay.height) // 2

    new_image = Image.new("RGB", background.size)

    new_image.paste(background, (0, 0))
    new_image.paste(overlay, (x, y))

    new_image.save(output_path, format='JPEG')


def is_9_16_aspect_ratio(image_path):
    image = Image.open(image_path)

    desired_aspect_ratio = 0.5625
    print(desired_aspect_ratio)
    aspect_ratio = image.width / image.height

    error_margin = 0.10

    return abs(aspect_ratio - desired_aspect_ratio) < error_margin


def main(image):

    background_image_path = image
    overlay_image_path = "icon.png"
    output_image_path = "imagem_1080.png"

    overlay_image_default(
        background_image_path, overlay_image_path, output_image_path
        )

    if is_9_16_aspect_ratio(image):
        overlay_image_path = image
        background_image_path = "background_story_vertical.png"
        output_image_path = "imagem_9_x_16_vertical.png"

        resize_and_overlay_story_vertical(
            background_image_path, overlay_image_path, output_image_path
            )
    else:
        overlay_image_path = image
        background_image_path = "background_story.png"
        output_image_path = "imagem_9_x_16_horizontal.png"

        resize_and_overlay_story(
            background_image_path, overlay_image_path, output_image_path
            )


images_for_test = ['foto_horizontal.jpeg', 'image_normal.png',
                   'image_after_genereted.jpg', 'foto_vertical.jpeg']
main(images_for_test[1])
