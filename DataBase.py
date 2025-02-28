import mysql.connector # Importa o módulo mysql.connector para conectar ao banco de dados MySQL

class Database:
    def __init__(self):
        # Conecta ao banco de dados MySQL com as credenciais fornecidas
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "ruandatabase_db"
        )
        self.cursor = self.conn.cursor() # Cria um cursor para executar comandos SQL
        
        # CRIA A TABELA "USUARIO" SE ELA NÃO EXISTIR

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
                idUsuario INT AUTO_INCREMENT PRIMARY KEY,
                nome TEXT(255),
                email TEXT(255),
                usuario TEXT (255),
                senha TEXT(255)        
                );''')
        self.conn.commit() # Confirma a criação da tabela

        print("Conectado ao banco de Dados!") # Imprime uma mensagem de confirmação

    # MÉTODO PARA REGISTRAR UM NOVO USUÁRIO NO BANCO DE DADOS

    def RegistrarNoBanco(self, nome, email, usuario, senha):
        self.cursor.execute("INSERT INTO usuario (nome, email, usuario, senha) VALUES (%s, %s, %s, %s)", (nome, email, usuario, senha)) #Insere os dados do usuário na tabela
        self.conn.commit() # Confirma a inserção dos dados
    
    # MÉTODO PARA ALTERAR OS DADOS DE UM USUÁRIO EXISTENTE NO BANCO DE DADOS

    def alterar(self, idUsuario, nome, email, usuario, senha):
        self.cursor.execute("UPDATE usuario SET nome = %s, email = %s, usuario = %s, senha = %s WHERE idUsuario = %s ",(nome, email, usuario, senha, idUsuario)) # Atualiza os dados do usuário com o id fornecido
        self.conn.commit() # Confirma a atualização dos dados

    # Método para excluir um usuário do banco de dados

    def excluir(self, idUsuario):
        self.cursor.execute("DELETE FROM usuario WHERE idUsuario = %s",(idUsuario)) #Exclui o usuário com o id fornecido
        self.conn.commit() # Confirma a exclusão dos dados

    # Método para buscar os dados de um usuário no banco de dados

    def buscar(self, idUsuario):
        self.cursor.execute("SELECT * FROM usuario WHERE idUsuario = %s", (idUsuario)) # Seleciona os dados do usuário com o id fornecido
        return self.cursor.fetchone() # Retorna os dados do usuário encontrado
    
    # Método chamado quando a instância da classe é destruida

    def __del__(self):
        self.conn.close() # Fecha a conexão com o banco de dados