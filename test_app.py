import unittest
from app import app
from flask import json

class TestApp(unittest.TestCase):

    # Método que é executado antes de cada teste
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_adicao_sitio_get(self):
        # Testar a requisição GET para a rota de adição de sítio
        response = self.app.get('/adicao_sitio')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cancelar', response.data) 

    def test_financeiro_get(self):
        # Testar a requisição GET para a rota de financeiro
        response = self.app.get('/financeiro')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Valor em Caixa', response.data) 

    def test_venda_balcao_get(self):
        # Testar a requisição GET para a rota de venda balcão
        response = self.app.get('/venda_balcao')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Caixas', response.data) 

    def test_fluxo_caixa_get(self):
        # Testar a requisição GET para a rota de fluxo de caixa
        response = self.app.get('/fluxo_caixa')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Fluxo de Caixa', response.data) 

    def test_reforco_caixa_get(self):
        # Testar a requisição GET para a rota de reforço de caixa
        response = self.app.get('/reforco_caixa')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Forma de Pagamento', response.data)

    def test_processar_reforco_post(self):
        # Testar a requisição POST para a rota de processar reforço
        response = self.app.post('/processar_reforco', data={
            'descricao_pagamento': 'Reforço Teste',
            'valor_reforco': '100.0',
            'forma_pagamento': 'Pix',
            'data_pagamento': '2024-10-07'
        })
        self.assertEqual(response.status_code, 302)  
        self.assertIn('/financeiro', response.location) 

    def test_sangria_caixa_get(self):
        # Testar a requisição GET para a rota de sangria de caixa
        response = self.app.get('/sangria_caixa')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sangria de Caixa', response.data)  

    def test_processar_sangria_post(self):
        # Testar a requisição POST para a rota de processar sangria
        response = self.app.post('/processar_sangria', data={
            'descricao_pagamento': 'Sangria Teste',
            'valor_sangria': '50.0',
            'forma_pagamento': 'Pix',
            'data_pagamento': '2024-10-07'
        })
        self.assertEqual(response.status_code, 302) 
        self.assertIn('/financeiro', response.location)  

if __name__ == '__main__':
    unittest.main()
