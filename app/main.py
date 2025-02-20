# app/main.py

import os
import time
import random
from whatsapp_driver import WhatsAppDriver
from whatsapp_mensagem import WhatsAppMensagem
from data_manager import GerenciadorDeDados


def main():
    # 1. Carregar dados
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    diretorio_data = os.path.join(
        diretorio_atual, "..", "data"
    )  # sobe um nível, pasta data/

    gerenciador_dados = GerenciadorDeDados(diretorio_data)
    lista_contatos = (
        gerenciador_dados.carregar_contatos()
    )  # ex: ["Cristiana", "Contato Exemplo 2", ...]
    mensagens = (
        gerenciador_dados.carregar_mensagens()
    )  # ex: {"mensagem_padrao": "...", "mensagem_promocional": "..."}
    configuracoes = (
        gerenciador_dados.carregar_configuracoes()
    )  # ex: {"caminho_pdf": "...", "caminho_perfil_chrome": "...", ...}

    # 2. Ler informações específicas
    mensagem_envio = mensagens["mensagem_padrao"]
    caminho_pdf = os.path.join(
        diretorio_atual, "..", "data", configuracoes["caminho_pdf"]
    )
    caminho_perfil_chrome = configuracoes["caminho_perfil_chrome"]
    diretorio_perfil_chrome = configuracoes["diretorio_perfil_chrome"]
    limite_erros_consecutivos = configuracoes["limite_erros_consecutivos"]

    # 3. Iniciar driver
    driver_manager = WhatsAppDriver(
        caminho_perfil_chrome, diretorio_perfil=diretorio_perfil_chrome
    )
    driver = driver_manager.iniciar_driver()

    # 4. Instanciar mensageria
    mensageria = WhatsAppMensagem(driver)
    mensageria.iniciar_whatsapp()

    # 5. Percorrer contatos e enviar
    erros_consecutivos = 0
    for contato in lista_contatos:
        try:
            sucesso = mensageria.enviar_mensagem_para_contato(
                contato, mensagem_envio, caminho_pdf
            )
            if sucesso:
                mensageria.resultados_envio[contato] = {
                    "status": "sucesso",
                    "erro": None,
                }
                erros_consecutivos = 0
        except Exception as erro:
            mensageria.resultados_envio[contato] = {"status": "erro", "erro": str(erro)}
            erros_consecutivos += 1
            print(f"Erro com {contato}: {erro}")
            if erros_consecutivos >= limite_erros_consecutivos:
                print("Limite de erros consecutivos atingido. Parando os envios.")
                break

        # Pausa para simular envio humano
        time.sleep(random.uniform(2, 4))

    # 6. Salvar resultados e manter aberto
    mensageria.salvar_resultados()
    print("Envios concluídos. Resultados salvos em 'resultados_envio.json'.")

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nProcesso encerrado manualmente.")
        driver_manager.finalizar_driver()


if __name__ == "__main__":
    main()
