import unittest
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from app import app
import time

# Função para iniciar o servidor Flask
def run_flask_app():
    app.run(port=5000)  # Altere a porta se necessário

class TestSelenium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Inicie o servidor Flask em um thread separado
        cls.flask_thread = Thread(target=run_flask_app)
        cls.flask_thread.daemon = True  # Permite que o thread seja encerrado quando o programa principal terminar
        cls.flask_thread.start()

        # Configure o driver do Chrome
        cls.driver = webdriver.Chrome()  
        cls.driver.implicitly_wait(10)

    def setUp(self):
        self.driver.get('http://127.0.0.1:5000/')  # URL do seu app Flask

    def test_adicao_sitio(self):
        self.driver.get('http://127.0.0.1:5000/adicao_sitio')

        # Localizar os campos do formulário e preencher
        produto_input = self.driver.find_element(By.NAME, 'produto')
        quantidade_input = self.driver.find_element(By.NAME, 'quantidade')
        data_input = self.driver.find_element(By.NAME, 'data')

        # Substitua pelos valores válidos do seu banco de dados
        produto_input.send_keys('Milho KG')  # Insira um produto existente
        quantidade_input.send_keys('25')
        data_input.send_keys('2024-05-18')  # Insira uma data válida

        # Enviar o formulário
        data_input.send_keys(Keys.RETURN)

        time.sleep(2)  # Esperar um pouco para que a página carregue (ou use WebDriverWait)

        # Verifique se a redireção ocorreu e se a adição foi bem-sucedida
        self.assertIn('Milho KG', self.driver.page_source)  # Certifique-se de que o texto correto está na página

    def test_venda_balcao(self):
        self.driver.get('http://127.0.0.1:5000/venda_balcao')

        # Localizar os campos do formulário e preencher
        cliente_input = self.driver.find_element(By.NAME, 'cliente')
        produto_input = self.driver.find_element(By.NAME, 'produto')
        quantidade_input = self.driver.find_element(By.NAME, 'quantidade')
        valor_venda_input = self.driver.find_element(By.NAME, 'valor_venda')
        forma_pagamento_input = self.driver.find_element(By.NAME, 'forma_pagamento')

        # Substitua pelos valores válidos do seu banco de dados
        cliente_input.send_keys('Cliente Teste')  # Insira um cliente existente
        produto_input.send_keys('Produto Teste')  # Insira um produto existente
        quantidade_input.send_keys('25')
        valor_venda_input.send_keys('33')  # Insira um valor válido
        forma_pagamento_input.send_keys('A vista')  # Ou outra forma de pagamento válida

        # Enviar o formulário
        forma_pagamento_input.send_keys(Keys.RETURN)

        time.sleep(2)  # Esperar um pouco para que a página carregue

        # Verifique se a venda foi registrada
        self.assertIn('Produto', self.driver.page_source)  # Certifique-se de que o texto correto está na página

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # Fechar o navegador após todos os testes

if __name__ == '__main__':
    unittest.main()
