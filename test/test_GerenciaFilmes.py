import unittest
from BancoFilmes.Gerenciadores.GerenciaFilmes import GerenciaFilmes
from test import UtilitariosTestes

pasta_teste = UtilitariosTestes.cria_ambiente_de_pastas_de_teste("gerencia_filmes")

class test_GerenciaFilmes(unittest.TestCase):
    def test_Instancia(self):
        conexao_banco_dados = UtilitariosTestes.conecta_banco_dados(pasta_teste, "gerencia_filmes", 1)
        gerenciador = GerenciaFilmes(conexao_banco_dados)
        self.assertIsInstance(gerenciador, GerenciaFilmes)


if __name__ == '__main__':
    unittest.main()
