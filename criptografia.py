import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
from PIL import Image, ImageTk
import os

global fernet, key, caminho_arquivo

def escolher_arquivo():
    global caminho_arquivo
    caminho_arquivo = filedialog.askopenfilename()
    if caminho_arquivo:
        label_arquivo.config(text=f"Arquivo selecionado: {caminho_arquivo}")

def encriptografar():
    global key, fernet
    key = Fernet.generate_key() # Chave salva aqui
    fernet = Fernet(key)
    if caminho_arquivo:
        with open(caminho_arquivo, "rb") as file:
            dados = file.read()
        dados_encriptados = fernet.encrypt(dados)
        with open(caminho_arquivo + ".enc", "wb") as file:
            file.write(dados_encriptados)
        salvar_key()
        label_arquivo.config(text="Arquivo encriptografado com sucesso!")

def descriptografar():
    global fernet, key
    if caminho_arquivo:
        caminho_key = os.path.splitext(caminho_arquivo)[0] + ".key"
    
        if not fernet:
            try:
                with open(caminho_key, "rb") as file:
                    key = file.read()
                fernet = Fernet(key)  # Define a chave correta antes de descriptografar
            except FileNotFoundError:
                label_arquivo.config(text="Erro: Chave não encontrada!")
                return

        # Lê o arquivo encriptado
        with open(caminho_arquivo + ".enc", "rb") as file:
            dados_encriptados = file.read()


        try:
            dados_descriptografados = fernet.decrypt(dados_encriptados)
            # Salva o arquivo descriptografado
            with open(caminho_arquivo + ".dec", "wb") as file:
                file.write(dados_descriptografados)
            label_arquivo.config(text="Arquivo descriptografado com sucesso!")
        except Exception:
            label_arquivo.config(text="Arquivo inválido!")

window = tk.Tk()
window.title("Encriptografar Arquivo")
window.geometry("700x500")

# Carregar a imagem de fundo (pode ser PNG, JPG, etc.)
imagem_fundo = Image.open("tela.png")
imagem_fundo = imagem_fundo.resize((700, 500), Image.BICUBIC)  # Redimensiona sem LANCZOS
bg_image = ImageTk.PhotoImage(imagem_fundo)

# Criar um label para exibir a imagem de fundo
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)  # Faz a imagem cobrir toda a tela


botao_selecionar = tk.Button(window, text="Escolher Arquivo", bg="#085178", fg="#edffa6", width=25, height=2, command=escolher_arquivo)
botao_selecionar.pack(pady=20)

label_arquivo = tk.Label(window, text="Nenhum arquivo selecionado")
label_arquivo.pack()


def salvar_key():
    global caminho_key
    # Remove a extensão do arquivo original
    caminho_key = os.path.splitext(caminho_arquivo)[0]
    with open(caminho_key + ".key", "wb") as file:
        file.write(key)

def escolher_key():
    global fernet
    caminho_key=filedialog.askopenfilename()
    if caminho_key:
        with open(caminho_key, "rb") as file:
            key = file.read()
    fernet = Fernet(key)  # Atualiza o objeto Fernet com a chave carregada
    label_key.config(text=f"Key selecionada: {caminho_key}")

def escolher_arquivo_enc():
    global caminho_arquivo
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos descriptografados", "*.enc")])
    if caminho_arquivo:
        label_arquivo.config(text=f"Arquivo selecionado: {caminho_arquivo}")

botao_selecionar_enc = tk.Button(window, text="Escolher Arquivo .enc", bg="#62C4D5", fg="#edffa6", width=25, height=2, command=escolher_arquivo_enc)
botao_selecionar_enc.pack(pady=20)


botao_encriptografar = tk.Button(window, text="Encriptografar", bg="#0077b6", fg="#edffa6", width=25, height=2, command=encriptografar)
botao_encriptografar.pack(pady=20)

botao_selecionar_key = tk.Button(window, text="Escolher Key", bg="#085178", fg="#edffa6", width=25, height=2, command=escolher_key)
botao_selecionar_key.pack(pady=20)

label_key = tk.Label(window, text="Nenhuma key selecionada")
label_key.pack()


botao_descriptografar = tk.Button(window, text="Descriptografar", bg="#62C4D5", fg="#edffa6", width=25, height=2, command=descriptografar)
botao_descriptografar.pack(pady=20)

window.mainloop()
