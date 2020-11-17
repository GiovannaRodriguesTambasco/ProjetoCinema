"""
Classe que facilita a conexão com o banco de dados usando SQLALchemy.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
class ConexaoBancoFilmes:
    """
    Classe que gerencia conexão com o banco de dados.
    """

    def __init__(self):
        self.conexao = None
        self.sessao = None
        self.tipo_banco_dados = ""
        self.usuario = ""
        self.senha = ""
        self.endereco = ""
        self.porta = ""
        self.banco_dados = ""

    def configura_conexao(self, tipo_banco_dados:str = "", usuario:str = "", senha:str = "", endereco:str = "", porta:str = "", banco_dados:str = ""):
        """
        Função que carrega os parâmetros de configuração com o banco de dados.

        :param tipo_banco_dados: str: Qual é o banco de dados? Postgre, SQLite, Oracle ou MySQL?
        :param usuario: Usuário do banco de dados.
        :param senha: Senha para conectar ao banco de dados.
        :param endereco: Endereço ou Ip para se conectar ao banco de dados.
        :param porta: A porta de comunicação com o banco de dados.
        :param banco_dados: Qual é o database para se conectar?
        :return:
        """
        self.tipo_banco_dados = tipo_banco_dados
        self.usuario = usuario
        self.senha = senha
        self.endereco = endereco
        self.porta = porta
        self.banco_dados = banco_dados

    def __gera_string_conexao(self) -> str:
        """
        Retorna a string de configuração para o SQLALchemy se conectar ao banco de dados.

        :return: str: Retorna string de configuração.
        """
        #Exemplo de uma string de configuração para o SQLALchemy.
        #'<tipo_banco_de_dados>://<Usuário>:<Senha>@<Endereço>:<porta>/<Database>'

        string_conexao = self.tipo_banco_dados + "://"
        #Se a string de usuário não for vazia, armazenará na string o nome de usuário
        if not self.usuario == "":
            string_conexao = string_conexao + self.usuario
        #Se o usuário tiver uma senha, armazenará na string a senha.
        if not self.senha == "":
            string_conexao = string_conexao + ":" + self.senha
        #Se a conexão tiver um endereço, armazenará na string o endereço
        if not self.endereco == "":
            string_conexao = string_conexao + "@" + self.endereco
        # Se a conexão precisar de uma porta personalizada
        #inser na string a porta
        if not self.porta == "":
            string_conexao = string_conexao + ":" + self.porta
        #Insere na string o banco de dados do servidor
        string_conexao = string_conexao + "/" + self.banco_dados
        return string_conexao

    def cria_conexao(self):
        if self.tipo_banco_dados.lower() == "sqlite":
            #Cria a engine de conexão do banco de dados
            self.conexao = create_engine(self.__gera_string_conexao() + "?check_same_thread=False")
            #Cria a sessão com o banco de dados
            sessao = sessionmaker(bind=self.conexao)
            self.sessao = scoped_session(sessao)

        else:
            #Cria a engine de conexão do banco de dados
            self.conexao = create_engine(self.__gera_string_conexao(), pool_recicle=1, max_overflow=0)
            # Cria a sessão com o banco de dados
            sessao = sessionmaker(bind=self.conexao)
            self.sessao = sessao()

    @property
    def get_sessao(self):
        return self.sessao

    @property
    def get_conexao(self):
        return self.conexao