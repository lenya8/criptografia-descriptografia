import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
from PIL import Image, ImageTk
import os #Verificação e manipulação de caminhos

# Variáveis globais
global fernet, key, caminho_arquivo, caminho_key
fernet = None
key = None
caminho_arquivo = None
caminho_key = None

def escolher_arquivo():
    #Seleciona um arquivo para criptografia ou descriptografia
    global caminho_arquivo
    caminho_arquivo = filedialog.askopenfilename()
    if caminho_arquivo:
        label_arquivo.config(text=f"Arquivo selecionado: {caminho_arquivo}")

def encriptografar():
    #Criptografa o arquivo selecionado e salva a chave automaticamente
    global key, fernet, caminho_arquivo
    if not caminho_arquivo:
        label_arquivo.config(text="Erro: Nenhum arquivo selecionado!")
        return

    key = Fernet.generate_key()
    fernet = Fernet(key)

    with open(caminho_arquivo, "rb") as file:
        dados = file.read()

    dados_encriptados = fernet.encrypt(dados)
    
    with open(caminho_arquivo + ".enc", "wb") as file:
        file.write(dados_encriptados)

    # Salvar a chave
    caminho_key = caminho_arquivo + ".key"
    with open(caminho_key, "wb") as file:
        file.write(key)

    label_arquivo.config(text="Arquivo encriptografado com sucesso!")

def escolher_key():
    #Permite ao usuário selecionar uma chave manualmente caso o carregamento automático falhe.
    global fernet, key, caminho_key
    caminho_key = filedialog.askopenfilename(filetypes=[("Chaves de Criptografia", "*.key")])
    if caminho_key:
        with open(caminho_key, "rb") as file:
            key = file.read()
        fernet = Fernet(key)
        label_key.config(text=f"Key selecionada: {caminho_key}")

def descriptografar():
    # Descriptografa um arquivo .enc usando a chave correspondente ou selecionada manualmente.
    global fernet, key, caminho_arquivo, caminho_key

    if not caminho_arquivo:
        label_arquivo.config(text="Erro: Nenhum arquivo selecionado!")
        return
    
    if not caminho_arquivo.endswith(".enc"):
        label_arquivo.config(text="Erro: Selecione um arquivo .enc!")
        return

    # Tentar carregar a chave automaticamente, se nenhuma chave manual foi escolhida
    if not caminho_key:
        caminho_key = os.path.splitext(caminho_arquivo)[0] + ".key"
    
    if os.path.exists(caminho_key):
        with open(caminho_key, "rb") as file:
            key = file.read()
        fernet = Fernet(key)
    else:
        label_arquivo.config(text="Erro: Chave não encontrada! Selecione uma manualmente.")
        return

    try:
        with open(caminho_arquivo, "rb") as file:
            dados_encriptados = file.read()

        dados_descriptografados = fernet.decrypt(dados_encriptados)

        caminho_descriptografado = caminho_arquivo.replace(".enc", ".dec")
        with open(caminho_descriptografado, "wb") as file:
            file.write(dados_descriptografados)

        label_arquivo.config(text="Arquivo descriptografado com sucesso!")
    except Exception:
        label_arquivo.config(text="Erro: Arquivo inválido ou chave incorreta!")

# Criando a interface gráfica
window = tk.Tk()
window.title("Criptografia de Arquivos")
window.geometry("700x500")

# Carregar a imagem de fundo (pode ser PNG, JPG, etc.)
imagem_fundo = Image.open("tela.png")
imagem_fundo = imagem_fundo.resize((700, 500), Image.BICUBIC)  # Redimensiona sem LANCZOS
bg_image = ImageTk.PhotoImage(imagem_fundo)

# Botões e labels

# Criar um label para exibir a imagem de fundo
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)  # Faz a imagem cobrir toda a tela

botao_selecionar = tk.Button(window, text="Escolher Arquivo", bg="#085178", fg="#f0bded", width=25, height=2, command=escolher_arquivo)
botao_selecionar.pack(pady=10)

label_arquivo = tk.Label(window, text="Nenhum arquivo selecionado")
label_arquivo.pack()

botao_encriptografar = tk.Button(window, text="Encriptografar", bg="#0077b6", fg="#f0bded", width=25, height=2, command=encriptografar)
botao_encriptografar.pack(pady=10)

botao_escolher_key = tk.Button(window, text="Selecionar Key Manualmente", bg="#f4a261", fg="#1c29e8", width=25, height=2, command=escolher_key)
botao_escolher_key.pack(pady=10)

label_key = tk.Label(window, text="Nenhuma key selecionada")
label_key.pack()

botao_descriptografar = tk.Button(window, text="Descriptografar", bg="#62C4D5", fg="#1c29e8", width=25, height=2, command=descriptografar)
botao_descriptografar.pack(pady=10)

# Iniciar o loop da interface gráfica
window.mainloop()