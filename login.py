from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database

jan = Tk() # Cria uma instância da janela principal
jan.title("RA Sytens - Painel de acesso") #Define o título da janela
jan.geometry("600x300") # Define o tamanho da janela
jan.configure(background = "white") # Configura a cor de fundo da janela
jan.resizable(width = False, height = False) # Impede que a janela seja redimensionada

# COMANDO PARA DEIXAR A TELA TRANSPARENTE 

jan.attributes("-alpha", 0.9) # Define a transparencia da janela (0.0 a 1.0)

# DEFINIR ÍCONE DA JANELA

# jan.iconbitmap(default = "icons/1logoIcon.ico") # Define o icone da janela

# CARREGAR IMAGEM 

# logo = PhotoImage(file = "icons/LogoSergio.png") # Carrega a imagem do logo

# CRIAR FRAME

LeftFrame = Frame(jan,width = 200, height = 300, bg = "MIDNIGHTBLUE", relief = "raise") # Cria um frame à esquerda

LeftFrame.pack(side = LEFT) # Posiciona o frame à esquerda

RightFrame = Frame(jan, width = 395, height = 300, bg = "MIDNIGHTBLUE", relief = "raise") # Cria um frame à direita

RightFrame.pack(side = RIGHT) # Posiciona o frame à direita

# ADICIONAR LOGO

# LogoLabel = Label(LeftFrame, image = logo, bg = "MIDNIGHTBLUE" ) # Cria um label para a imagem do logo

# LogoLabel.place(x = 50, y = 100) # Posiciona o label no frame esquerdo

# ADICIONAR CAMPOS DE USUÁRIO E SENHA

UsuarioLabel = Label(RightFrame, text = "Usuario: ", font =("Century Gothic", 20), bg = "MIDNIGHTBLUE", fg = "White") # Cria um label para o usuário
UsuarioLabel.place(x = 5, y = 100) # Posiciona o label no frame direito

UsuarioEntry = ttk.Entry(RightFrame, width = 30) # Criar um campo de entrada para o usuário
UsuarioEntry.place (x = 120, y = 115) # Posiciona o campo de entrada

SenhaLabel = Label(RightFrame, text = "Senha: ", font=("Century Gothic", 20), bg = "MIDNIGHTBLUE", fg = "White") # Cria um label para a senha
SenhaLabel.place(x = 5, y = 150) # Posiciona o label no frame direito

SenhaEntry = ttk.Entry(RightFrame, width = 30, show = "•") # Cria um campo de entrada para a senha
SenhaEntry.place(x = 120, y = 165) # Posiciona o campo de entrada

# FUNÇÃO DE LOGIN

def Login():
    usuario = UsuarioEntry.get() # Obtém o valor do campo de entrada do usuário
    senha = SenhaEntry.get() # Obtém o valor do campo de entrada da senha

    # Conectar ao banco de dados
    db = Database() # Cria uma instância da classe Database
    db.cursor.execute("SELECT * FROM usuario WHERE usuario = %s AND senha = %s", (usuario, senha)) # Executa a consulta SQL para verificar o usuário e a senha
    VerifyLogin = db.cursor.fetchone() # Obtém o resultado da consulta

    # Verificar se o usuário foi encontrado
    if VerifyLogin:
        messagebox.showinfo(title = "INFO LOGIN", message = "Acesso confirmado. Seja bem vindo!") # Exibe mensagem de sucesso
    else:
        messagebox.showinfo(title = "INFO LOGIN", message = "Acesso negado. Verifique se está cadastrado no Sistema!") #Exibe mensagem de erro.

# CRIANDO BOTÕES
LoginButton = ttk.Button(RightFrame, text = "LOGIN", width = 15, command = Login) # Cria um botão de login
LoginButton.place(x = 150, y = 225) # Posiciona o botão de login

# FUNÇÃO PARA REGISTRAR NOVO USUÁRIO
def Registrar():
    # REMOVENDO BOTÕES DE LOGIN
    LoginButton.place(x = 5000) # Move o botão de login para fora da tela
    RegisterButton.place(x = 5000) # Move o botão de registro para fora da tela

    # INSRINDO WIDGETS DE CADASTRO
    NomeLabel = Label(RightFrame, text = "Nome: ", font= ("Century Gothic", 20), bg = "MIDNIGHTBLUE", fg = "White") # Cria um label para o nome
    NomeLabel.place(x = 5, y = 5) # Posiciona o campo de entrada

    NomeEntry = ttk.Entry(RightFrame, width = 30) # Cria um campo de entrada para o nome
    NomeEntry.place(x = 120, y = 20) # Posiciona o campo de entrada

    EmailLabel = Label(RightFrame, text = "Email: ", font = ("Century Gothic", 20), bg = "MIDNIGHTBLUE", fg = "White") # Cria um label para o e-mail
    EmailLabel.place(x = 5, y = 40) # Posiciona o label no frame direito

    EmailEntry = ttk.Entry(RightFrame, width = 30) # Cria um campo de entrada para o e-mail
    EmailEntry.place(x = 120, y = 55) # Posiciona o campo de entrada

    # FUNÇÃO PARA REGISTRAR NO BANCO DE DADOS
    def RegistrarNoBanco():
        nome = NomeEntry.get() # Obtém o valor do campo de entrada do nome
        email = EmailEntry.get() # Obtém o valor do campo de entrada do email
        usuario = UsuarioEntry.get() # Obtém o valor do campo de entrada do usuário
        senha = SenhaEntry.get() # Obtém o valor do campo de entrada da senha

        # Verifica se todos os campos estão preenchidos
        if nome == "" or email == "" or usuario == "" or senha == "":
            messagebox.showerror(title = "Erro de Registro", message = "PREENCHA TODOS OS CAMPOS") # Exibe mensagem de erro