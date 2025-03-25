# Criptografia-descriptografia

O código utiliza Python e a biblioteca cryptography para criptografar e descriptografar de forma simétrica. A interface permite que o usuário selecione um arquivo e criptografe o mesmo. O usuário também pode selecionar um arquivo com a extensão .enc e descriptografar ele, gerando um arquivo com a extensão .dec. Pode ser feita a seleção de uma chave específica. A interface é disponibilizada a partir do uso do Tkinter.

# Funcionalidades
* Selecionar um arquivo para criptografar.
* Gerar a chave para criptografar e salvar ela no mesmo diretório do arquivo original.
* Criptografar o arquivo original e gerar um arquivo .enc.
* Selecionar manualmente uma chave para descriptografar se for desejado.
* Descriptografar arquivos .enc.

# Tecnologias utilizadas
* Python
* Tkinter (Interface Gráfica)
* Cryptography (Fernet para criptografia)
* Pillow (Manipulação de imagens para fundo da interface)

# Como executar
Instale as dependências necessárias (pip install cryptography) e execute o script Python. Utilize a interface para selecionar um arquivo, criptografá-lo ou descriptografá-lo. Se necessário, selecione a chave a ser utilizada.
