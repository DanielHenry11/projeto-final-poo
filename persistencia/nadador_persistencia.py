from typing import List
from modelos.nadador import Nadador
from persistencia.gerenciador_json import GerenciadorJSON

class NadadorPersistencia:
    def __init__(self, caminho_arquivo: str = "dados/nadadores.json") -> None:
        self.caminho_arquivo = caminho_arquivo

    def salvar_todos(self, nadadores: List[Nadador]) -> None:
        dados = [
            {"nome": n.nome, "matricula": n.matricula}
            for n in nadadores
        ]
        GerenciadorJSON.salvar(self.caminho_arquivo, dados)

    def carregar_todos(self) -> List[Nadador]:
        dados = GerenciadorJSON.carregar(self.caminho_arquivo) or []
        nadadores = []
        for item in dados:
            nadador = Nadador(item["nome"], item["matricula"])
            nadadores.append(nadador)
        return nadadores