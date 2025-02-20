from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurações para usar um perfil do Chrome já logado no WhatsApp Web
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=/home/vinicius/.config/google-chrome")
chrome_options.add_argument("profile-directory=Default")

# Inicia o driver do Chrome com as opções definidas
driver = webdriver.Chrome(options=chrome_options)

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com")

# Função para simular digitação humana
def digitar_com_delay(element, texto):
    for letra in texto:
        element.send_keys(letra)
        time.sleep(random.uniform(0.05, 0.2))  # atraso aleatório entre letras

# Nome do contato
nome_contato = "Cristiana"

# Aguarda o WhatsApp carregar antes de buscar o contato
while True:
    try:
        search_box = driver.find_element(By.CSS_SELECTOR, 'div[contenteditable="true"][data-tab="3"]')
        break  # Sai do loop se encontrou o elemento
    except:
        time.sleep(1)  # Aguarda um pouco antes de tentar novamente

search_box.click()
search_box.send_keys(nome_contato)

while True:
    try:
        contato = driver.find_element(By.CSS_SELECTOR, f'span[title="{nome_contato}"]')
        contato.click()
        break  # Sai do loop se encontrou o contato
    except:
        time.sleep(10)  # Aguarda antes de tentar novamente

# Envio da mensagem
message_box = driver.find_element(By.CSS_SELECTOR, 'div[contenteditable="true"][data-tab="10"]')
mensagem = "Olá, esta é uma mensagem automatizada!"
digitar_com_delay(message_box, mensagem)

# Aguarda até que o botão de envio esteja visível e clicável
send_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Enviar"]'))
)
send_button.click()

time.sleep(10) 


# Aguarda até que o botão de anexar esteja visível e clicável
attachment_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="Anexar"]'))
)
attachment_button.click()

# Aguarda até que o campo de entrada do arquivo apareça
file_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]'))
)

# Obtém o diretório do script atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho completo do arquivo PDF
caminho_pdf = os.path.join(diretorio_atual, "curriculo-vinicius-franco-jan-2025-1-1.pdf")

# Enviar o arquivo no WhatsApp Web
file_input.send_keys(caminho_pdf)

# Aguarda até que o botão de envio do arquivo esteja visível e clicável
send_pdf_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@role="button" and @aria-label="Enviar"]'))
)
send_pdf_button.click()

# Mantém o navegador aberto sem finalizar o processo
print("WhatsApp Web automatizado está rodando... Pressione Ctrl+C para encerrar.")

try:
    while True:
        time.sleep(10)  # Mantém o script ativo sem consumir muita CPU
except KeyboardInterrupt:
    print("\nProcesso encerrado manualmente.")
