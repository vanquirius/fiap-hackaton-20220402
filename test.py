# coding=utf-8
# Hackaton FIAP
# Enilson dos Santos Jr., Klaus Araújo, Lilian Barbosa, Marcelo Góes,
# Müller Silva, Nicolas Osmundo, Roberto Ribeiro, Vinicius Montouro
# 2022-04-02

from app import app
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

        # envia uma requisicao GET para a URL
        self.result = self.app.get('/')

    def test_requisicao(self):
        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result.status_code, 200)

    def test_conteudo(self):
        # verifica o retorno do conteudo da pagina
        with open("html/index.html", mode="r") as f:
            html_content = f.read()
        self.assertEqual(self.result.data.decode('utf-8'), html_content)