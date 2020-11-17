import os
from BancoFilmes.ConexaoBancoFilmes import ConexaoBancoFilmes


def cria_pastas(pasta_teste: str) -> bool:
    """
    Cria pasta

    :param pasta_teste: Caminho absoluto da pasta.
    :return:
    """
    if isinstance(pasta_teste, str):
        if not os.path.exists(pasta_teste):
            os.mkdir(pasta_teste)
        return True
    return False

def cria_ambiente_de_pastas_de_teste(teste: str) -> str:
    """
    Cria ambiente limpo para testes.

    :param teste: Nome do teste.
    :return: Caminho absoluto da pasta de teste.
    """
    if isinstance(teste, str):
        # Cria a estrutura de pastas dos testes
        cria_pastas("C:\\temp")
        cria_pastas("C:\\temp\\Projeto_Cinema")
        pasta_teste = "C:\\temp\\Projeto_Cinema\\" + teste + "\\"
        cria_pastas(pasta_teste)
        # Se a pasta de teste já conter algum arquivo, apagará todos
        apaga_arquivos(pasta_teste)
        return pasta_teste


def conecta_banco_dados(pasta_teste:str,teste:str,numero_teste:str):
    """
    Retorna a conexão com o banco de dados.

    :param pasta_teste: Caminho absoluto da pasta de testes.
    :param teste: Nome do teste.
    :param numero_teste: Número do teste.
    :return:
    """

    #Criando a conexão com o banco de dados.
    banco_dados = ConexaoBancoFilmes()
    banco_dados.configura_conexao(tipo_banco_dados="sqlite",banco_dados=pasta_teste + teste + "_"+ str(numero_teste) + ".db")
    banco_dados.cria_conexao()
    return banco_dados

def apaga_arquivos(pasta_teste):
    """
    Limpa o conteúdo da pasta onde será armazenado os arquivos de teste.

    :param pasta_teste: Caminho absoluto até a pasta de testes.
    :return:
    """
    if isinstance(pasta_teste,str):
        for itens in os.listdir(pasta_teste):
            if os.path.isfile(os.path.join(pasta_teste, itens)):
                os.remove(pasta_teste + itens)