from tkinter import *
from tkinter import ttk
from main import *
from image_loader import load_rounded_button_image  # Importe a função
import os

tema_claro = False

def atualizar_tema():
    global tema_claro
    global janela_principal
    global pagina1
    global pagina2
    global botao_mudar_fundo_pagina1

    cor_fundo = "#fff" if tema_claro else "#454545"
    texto_botao_tema = "Mudar para Claro" if tema_claro else "Mudar para Escuro"

    janela_principal.config(bg=cor_fundo)
    pagina1.config(bg=cor_fundo)
    pagina2.config(bg=cor_fundo)
    botao_mudar_fundo_pagina1.config(text=texto_botao_tema)

def mudar_fundo():
    global tema_claro
    tema_claro = not tema_claro
    atualizar_tema()

def mostrar_pagina2():
    pagina1.grid_forget()
    pagina2.grid(row=0, column=0, sticky="nsew")

def mostrar_pagina1():
    pagina2.grid_forget()
    pagina1.grid(row=0, column=0, sticky="nsew")


janela_principal = Tk()
janela_principal.geometry("800x800")
janela_principal.title("Timer")
janela_principal.config(bg="#454545")

# Carregue a imagem usando a função importada
image_path = os.path.join("Images", "arredondado.png")
imagem_tk = load_rounded_button_image(image_path)

# Página 1
pagina1 = Frame(janela_principal, bg="#454545")
botao_mudar_fundo_pagina1 = Button(pagina1, text="Mudar para Claro" if tema_claro else "Mudar para Escuro", command=mudar_fundo)
botao_mudar_fundo_pagina1.grid(row=0, column=0, padx=10, pady=10)

botao_mudar_tela_pagina1 = Button(pagina1, image=imagem_tk, borderwidth=0, highlightthickness=0, command=mostrar_pagina2, background="#454545", activebackground="#454545", relief=FLAT)
if imagem_tk:
    pass
botao_mudar_tela_pagina1.grid(row=1, column=0, padx=10, pady=10)
pagina1.grid(row=0, column=0, sticky="nsew")

# Página 2
pagina2 = Frame(janela_principal, bg="#454545")
texto_pagina2 = Label(pagina2,text="Esta é a Página 2", background="#454545", fg="#fff")
texto_pagina2.grid(row=0, column=0, padx=20, pady=20)
botao_voltar_pagina1 = Button(pagina2, text="Voltar para Tela 1", command=mostrar_pagina1)
botao_voltar_pagina1.grid(row=1, column=0, padx=10, pady=10)

janela_principal.grid_columnconfigure(0, weight=1)
janela_principal.grid_rowconfigure(0, weight=1)

janela_principal.mainloop()