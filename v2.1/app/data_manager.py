# app/data_manager.py

import os
import json


class GerenciadorDeDados:
    def __init__(self, diretorio_data):
        """
        :param diretorio_data: Caminho para a pasta onde estão os arquivos JSON.
        """
        self.diretorio_data = diretorio_data

    def carregar_contatos(self):
        """Carrega a lista de contatos a partir de contatos.json."""
        caminho_contatos = os.path.join(self.diretorio_data, "contatos.json")
        with open(caminho_contatos, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)  # Retorna lista de contatos

    def carregar_mensagens(self):
        """Carrega mensagens a partir de mensagens.json."""
        caminho_mensagens = os.path.join(self.diretorio_data, "mensagens.json")
        with open(caminho_mensagens, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)  # Retorna dicionário com mensagens

    def carregar_configuracoes(self):
        """Carrega configurações gerais a partir de configuracoes.json."""
        caminho_configuracoes = os.path.join(self.diretorio_data, "configuracoes.json")
        with open(caminho_configuracoes, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)  # Retorna dicionário com configs
