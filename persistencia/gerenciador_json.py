import json
import os
from typing import List, Dict, Any

class GerenciadorJSON:

    @staticmethod
    def salvar(caminho_arquivo: str, dados: List[Dict[Any, Any]]) -> None:
        """Salva uma lista de dicionários em um arquivo JSON."""
        with open(caminho_arquivo, "w", encoding="utf-8") as file:
            json.dump(dados, file, ensure_ascii=False, indent=4)

    @staticmethod
    def carregar(caminho_arquivo: str) -> List[Dict[Any, Any]]:
        """Carrega dados de um arquivo JSON. Retorna lista vazia se não existir."""
        if not os.path.exists(caminho_arquivo):
            return []
        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []