from PIL import Image


def overlay_image(background_path, overlay_path, output_path):
    background = Image.open(background_path)
    overlay = Image.open(overlay_path)

    # No meio em baixo 20px de distância
    x = (background.width - overlay.width) // 2
    y = background.height - overlay.height - 20

    # Crie uma nova imagem com o mesmo tamanho da imagem de fundo
    new_image = Image.new("RGBA", background.size, (0, 0, 0, 0))

    # Cole a imagem de fundo e a imagem de sobreposição na nova imagem
    new_image.paste(background, (0, 0))
    new_image.paste(overlay, (x, y), overlay)

    # Salve a imagem resultante em PNG para preservar a transparência
    new_image.save(output_path)


def resize_and_overlay(background_path, overlay_path, output_path):
    # Abre as imagens usando a biblioteca Pillow
    background = Image.open(background_path)
    overlay = Image.open(overlay_path)

    # Redimensiona a imagem "image_normal.png" para
    # ter a largura de 1620 pixels
    target_width = 1620
    width_percent = (target_width / float(overlay.width))
    target_height = int((float(overlay.height) * float(width_percent)))
    overlay = overlay.resize((target_width, target_height), Image.LANCZOS)

    # Remove o canal alfa da imagem, se for RGBA (imagens PNG com transparência)
    if overlay.mode in ('RGBA', 'LA') or (overlay.mode == 'P' and 'transparency' in overlay.info):
        overlay = overlay.convert('RGB')

    # Calcula a posição para colocar a imagem de sobreposição no meio do background
    x = (background.width - overlay.width) // 2
    y = (background.height - overlay.height) // 2

    # Crie uma nova imagem com o mesmo tamanho do background
    new_image = Image.new("RGB", background.size)

    new_image.paste(background, (0, 0))
    new_image.paste(overlay, (x, y))

    # Salve a imagem resultante em JPEG
    new_image.save(output_path, format='PNG')


background_image_path = "image_after_genereted.jpg"
overlay_image_path = "icon.png"
output_image_path = "imagem_1_x_1.png"

overlay_image(background_image_path, overlay_image_path, output_image_path)

background_image_path = "background_story.png"
overlay_image_path = "image_after_genereted.jpg"
output_image_path = "imagem_9_x_16.png"

resize_and_overlay(background_image_path, overlay_image_path, output_image_path) 