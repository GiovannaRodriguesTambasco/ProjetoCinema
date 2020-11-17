from BancoFilmes.ConexaoBancoFilmes import ConexaoBancoFilmes
from BancoFilmes.ORMs.FilmesORM import Filmes, cria_tabelas

class GerenciaFilmes:
    def __init__(self, conexao_banco_filmes: ConexaoBancoFilmes):
        self.conexao_banco_filmes = conexao_banco_filmes
        cria_tabelas(self.conexao_banco_filmes.get_conexao)

    def novo_filme(self, nome: str, publicado_em: str, sinopse: str, idade_minima: int, genero: int, em_3d: bool):
        """
        Cria um novo filme.

        :param nome: Nome do filme
        :param publicado_em: Data de publicação
        :param sinopse: Sinopse do filme
        :param idade_minima: Idade mínima do filme
        :param genero: Gênero do filme
        :param em_3d: O filme é em 3d?
        :return:
        """

        filme = Filmes()
        filme.nome = nome
        filme.publicado_em = publicado_em
        filme.sinopse = sinopse
        filme.idade_minima = idade_minima
        filme.genero = genero
        filme.em_3d = em_3d

        self.conexao_banco_filmes.get_sessao.add(filme)
        self.conexao_banco_filmes.get_sessao.commit()
        return filme.id_filme