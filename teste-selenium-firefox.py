from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurações para usar um perfil do Chrome já logado no WhatsApp Web
chrome_options = webdriver.ChromeOptions()

# Substitua pelo caminho do diretório de dados do Chrome (onde os perfis ficam armazenados)
# Exemplo no Linux:
chrome_options.add_argument("user-data-dir=/home/vinicius/.config/google-chrome")

# Se você tiver vários perfis, especifique a pasta do perfil. Normalmente, o padrão é "Default"
chrome_options.add_argument("profile-directory=Default")

# Inicia o driver do Chrome com as opções definidas
driver = webdriver.Chrome(options=chrome_options)

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com")

# Aguarde alguns segundos para o carregamento completo (ajuste se necessário)
time.sleep(30)

# Continue com suas interações...
