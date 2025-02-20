from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random

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
time.sleep(15)

# Função para simular digitação humana
def digitar_com_delay(element, texto):
    for letra in texto:
        element.send_keys(letra)
        time.sleep(random.uniform(0.05, 0.2))  # atraso aleatório entre letras

# Nome do contato (exatamente como aparece no WhatsApp)
nome_contato = "Nome do Contato"

# Localiza a caixa de busca de contatos
# O XPATH pode variar; atualize se necessário
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
time.sleep(random.uniform(1, 2))
search_box.send_keys(nome_contato)
time.sleep(2)

# Seleciona o contato na lista de resultados
contato = driver.find_element(By.XPATH, f'//span[@title="{nome_contato}"]')
contato.click()
time.sleep(random.uniform(1, 2))

# Envia mensagem de texto
message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
mensagem = "Olá, esta é uma mensagem automatizada!"
digitar_com_delay(message_box, mensagem)
time.sleep(random.uniform(0.5, 1))
# Clica no botão de enviar (às vezes o Enter funciona também)
send_button = driver.find_element(By.XPATH, '//button[@data-testid="compose-btn-send"]')
send_button.click()
time.sleep(2)

# Envio de arquivo PDF
# 1. Clica no ícone de anexo
attachment_button = driver.find_element(By.XPATH, '//div[@title="Anexar"]')
attachment_button.click()
time.sleep(random.uniform(1, 2))

# 2. Seleciona o input de arquivo (o XPATH pode precisar de ajustes)
file_input = driver.find_element(By.XPATH, '//input[@accept="*"]')
# Caminho absoluto do arquivo PDF que deseja enviar
caminho_pdf = "/caminho/para/o/arquivo.pdf"
file_input.send_keys(caminho_pdf)
time.sleep(random.uniform(1, 2))

# 3. Clica no botão de envio do PDF
send_pdf_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
send_pdf_button.click()
time.sleep(2)

# Encerra o driver (opcional)
# driver.quit()
