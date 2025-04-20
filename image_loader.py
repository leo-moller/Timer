from PIL import Image, ImageTk
import os

def load_rounded_button_image(image_path):
    try:
        imagem_pil = Image.open(image_path)
        imagem_tk = ImageTk.PhotoImage(imagem_pil)
        return imagem_tk
    except FileNotFoundError:
        print(f"Erro: A imagem do botão não foi encontrada em: {image_path}")
        return None