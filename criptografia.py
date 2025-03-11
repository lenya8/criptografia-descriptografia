import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
from PIL import Image, ImageTk

def escolher_arquivo():
    global caminho_arquivo
    caminho_arquivo = filedialog.askopenfilename()
    if caminho_arquivo:
        label_arquivo.config(text=f"Arquivo selecionado: {caminho_arquivo}")

def encriptografar():
    if caminho_arquivo:
        with open(caminho_arquivo, "rb") as file:
            dados = file.read()
        dados_encriptados = fernet.encrypt(dados)
        with open(caminho_arquivo + ".enc", "wb") as file:
            file.write(dados_encriptados)
        label_arquivo.config(text="Arquivo encriptografado com sucesso!")

def descriptografar():
    if caminho_arquivo:
        with open(caminho_arquivo + ".enc", "rb") as file:
            dados_encriptados = file.read()
        dados_descriptografados = fernet.decrypt(dados_encriptados)
        with open(caminho_arquivo + ".dec", "wb") as file:
            file.write(dados_descriptografados)
        label_arquivo.config(text="Arquivo descriptografado com sucesso!")

window = tk.Tk()
window.title("Encriptografar/Descriptografar Arquivo")
window.geometry("700x500")

imagem_fundo = Image.open("criptografia.png")
imagem_fundo = imagem_fundo.resize((700, 500), Image.BICUBIC)  # Redimensiona sem LANCZOS
bg_image = ImageTk.PhotoImage(imagem_fundo)

bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)  # Faz a imagem cobrir toda a tela

botao_selecionar = tk.Button(window, text="Escolher Arquivo", bg="purple", fg="blue", width=25, height=2, command=escolher_arquivo)
botao_selecionar.pack(pady=20)

label_arquivo = tk.Label(window, text="Nenhum arquivo selecionado")
label_arquivo.pack()

key = Fernet.generate_key() # Chave salva aqui
fernet = Fernet(key)

botao_encriptografar = tk.Button(window, text="Encriptografar", bg="blue", fg="blue", width=25, height=2, command=encriptografar)
botao_encriptografar.pack(pady=20)

botao_descriptografar = tk.Button(window, text="Descriptografar", bg="green", fg="blue", width=25, height=2, command=descriptografar)
botao_descriptografar.pack(pady=20)

window.mainloop()
