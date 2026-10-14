from typing import List
from modelos.toalha import Toalha
from persistencia.gerenciador_json import GerenciadorJSON

class ToalhaPersistencia:
    def __init__(self, caminho_arquivo: str = "dados/toalhas.json") -> None:
        self.caminho_arquivo = caminho_arquivo

    def salvar_todas(self, toalhas: List[Toalha]) -> None:
        dados = [
            {"codigo": t.codigo, "disponivel": t.disponivel}
            for t in toalhas
        ]
        GerenciadorJSON.salvar(self.caminho_arquivo, dados)

    def carregar_todas(self) -> List[Toalha]:
        dados = GerenciadorJSON.carregar(self.caminho_arquivo) or []
        toalhas = []
        for item in dados:
            toalha = Toalha(item["codigo"])
            toalha.disponivel = item.get("disponivel", True)
            toalhas.append(toalha)
        return toalhas