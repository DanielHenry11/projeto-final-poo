from typing import List
from modelos.atendente import Atendente
from persistencia.gerenciador_json import GerenciadorJSON

class AtendentePersistencia:
    def __init__(self, caminho_arquivo: str = "dados/atendentes.json") -> None:
        self.caminho_arquivo = caminho_arquivo

    def salvar_todos(self, atendentes: List[Atendente]) -> None:
        dados = [
            {"nome": a.nome}
            for a in atendentes
        ]
        GerenciadorJSON.salvar(self.caminho_arquivo, dados)

    def carregar_todos(self) -> List[Atendente]:
        dados = GerenciadorJSON.carregar(self.caminho_arquivo) or []
        atendentes = []
        for item in dados:
            atendente = Atendente(item["nome"])
            atendentes.append(atendente)
        return atendentes