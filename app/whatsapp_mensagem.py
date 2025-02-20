# whatsapp_mensagem.py
import time
import random
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WhatsAppMensagem:
    def __init__(self, driver, tempo_delay_min=0.05, tempo_delay_max=0.2):
        """
        Inicializa a classe responsável pelas ações no WhatsApp Web.

        :param driver: Instância do Selenium WebDriver.
        :param tempo_delay_min: Delay mínimo entre caracteres (simula digitação).
        :param tempo_delay_max: Delay máximo entre caracteres.
        """
        self.driver = driver
        self.tempo_delay_min = tempo_delay_min
        self.tempo_delay_max = tempo_delay_max
        self.resultados_envio = {}

    def limpar_caixa_texto(self, elemento):
        """Limpa o conteúdo de uma caixa de texto (elemento contenteditable)."""
        elemento.send_keys(Keys.CONTROL, "a")
        time.sleep(0.1)
        elemento.send_keys(Keys.DELETE)

    def digitar_texto_com_delay(self, elemento, texto):
        """Simula digitação humana, enviando um caractere por vez com delay."""
        for caractere in texto:
            elemento.send_keys(caractere)
            time.sleep(random.uniform(self.tempo_delay_min, self.tempo_delay_max))

    def iniciar_whatsapp(self):
        """Abre o WhatsApp Web e aguarda o carregamento da caixa de busca."""
        self.driver.get("https://web.whatsapp.com")
        while True:
            try:
                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'div[contenteditable="true"][data-tab="3"]')
                    )
                )
                break
            except Exception:
                time.sleep(1)

    def enviar_mensagem_para_contato(self, nome_contato, mensagem, caminho_arquivo_pdf):
        """
        Envia mensagem e anexa um arquivo PDF para o contato especificado.

        :param nome_contato: Nome do contato conforme exibido no WhatsApp.
        :param mensagem: Mensagem de texto a ser enviada.
        :param caminho_arquivo_pdf: Caminho completo do arquivo PDF a ser anexado.
        :return: True se o envio for bem-sucedido.
        :raises Exception: Em caso de erro durante algum passo.
        """
        try:
            # Localiza e limpa a caixa de busca, em seguida digita o nome do contato.
            caixa_busca = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'div[contenteditable="true"][data-tab="3"]')
                )
            )
            caixa_busca.click()
            self.limpar_caixa_texto(caixa_busca)
            caixa_busca.send_keys(nome_contato)
            time.sleep(2)  # aguarda atualização da lista

            # Seleciona o contato
            contato = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, f'span[title="{nome_contato}"]')
                )
            )
            contato.click()
            time.sleep(2)

            # Envia mensagem de texto
            caixa_mensagem = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'div[contenteditable="true"][data-tab="10"]')
                )
            )
            caixa_mensagem.click()
            self.limpar_caixa_texto(caixa_mensagem)
            self.digitar_texto_com_delay(caixa_mensagem, mensagem)
            time.sleep(random.uniform(0.5, 1.0))

            botao_enviar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Enviar"]')
                )
            )
            botao_enviar.click()
            time.sleep(random.uniform(1.0, 2.0))

            # Anexa o arquivo PDF
            botao_anexar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="Anexar"]'))
            )
            botao_anexar.click()
            time.sleep(1)

            campo_arquivo = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]'))
            )
            campo_arquivo.send_keys(caminho_arquivo_pdf)
            time.sleep(2)

            botao_enviar_arquivo = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[@role="button" and @aria-label="Enviar"]')
                )
            )
            botao_enviar_arquivo.click()
            time.sleep(2)

            return True

        except Exception as erro:
            raise Exception(f"Erro ao enviar mensagem para {nome_contato}: {erro}")

    def salvar_resultados(self, caminho_json="resultados_envio.json"):
        """Salva os resultados dos envios em um arquivo JSON."""
        with open(caminho_json, "w", encoding="utf-8") as arquivo:
            json.dump(self.resultados_envio, arquivo, ensure_ascii=False, indent=4)
