# whatsapp_driver.py
from selenium import webdriver


class WhatsAppDriver:
    def __init__(self, caminho_perfil_chrome, diretorio_perfil="Default"):
        """
        Inicializa o gerenciador do driver do Selenium.

        :param caminho_perfil_chrome: Caminho para o diretório do perfil do Chrome.
        :param diretorio_perfil: Nome do diretório do perfil (padrão "Default").
        """
        self.caminho_perfil_chrome = caminho_perfil_chrome
        self.diretorio_perfil = diretorio_perfil
        self.driver = None

    def iniciar_driver(self):
        """Configura e inicia o driver do Selenium com o perfil especificado."""
        opcoes = webdriver.ChromeOptions()
        opcoes.add_argument(f"user-data-dir={self.caminho_perfil_chrome}")
        opcoes.add_argument(f"profile-directory={self.diretorio_perfil}")
        self.driver = webdriver.Chrome(options=opcoes)
        return self.driver

    def finalizar_driver(self):
        """Finaliza o driver, fechando o navegador."""
        if self.driver:
            self.driver.quit()
