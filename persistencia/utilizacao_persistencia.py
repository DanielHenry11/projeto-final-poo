from typing import List, Dict
from modelos.utilizacao import Utilizacao
from modelos.nadador import Nadador
from modelos.toalha import Toalha
from modelos.atendente import Atendente
from persistencia.gerenciador_json import GerenciadorJSON

class UtilizacaoPersistencia:
    def __init__(self, caminho_arquivo: str = "dados/utilizacoes.json") -> None:
        self.caminho_arquivo = caminho_arquivo

    def salvar_todas(self, utilizacoes: List[Utilizacao]) -> None:
        dados = []
        for u in utilizacoes:
            atendente_entrega_nome = getattr(u, "atendente_entrega", getattr(u, "atendente", None))
            atendente_entrega_str = atendente_entrega_nome.nome if atendente_entrega_nome else ""

            atendente_devolucao_nome = getattr(u, "atendente_devolucao", None)
            atendente_devolucao_str = atendente_devolucao_nome.nome if atendente_devolucao_nome else ""

            dados.append({
                "nadador_matricula": u.nadador.matricula,
                "toalha_codigo": u.toalha.codigo,
                "atendente_entrega_nome": atendente_entrega_str,
                "atendente_devolucao_nome": atendente_devolucao_str,
                "aberta": u.aberta
            })
            
        GerenciadorJSON.salvar(self.caminho_arquivo, dados)

    def carregar_todas(
        self,
        nadadores_dict: Dict[str, Nadador],
        toalhas_dict: Dict[str, Toalha],
        atendentes_dict: Dict[str, Atendente]
    ) -> List[Utilizacao]:
        dados = GerenciadorJSON.carregar(self.caminho_arquivo) or []
        utilizacoes = []

        for item in dados:
            nadador = nadadores_dict.get(item["nadador_matricula"])
            toalha = toalhas_dict.get(item["toalha_codigo"])
            atendente_entrega = atendentes_dict.get(item["atendente_entrega_nome"])

            if nadador and toalha and atendente_entrega:
                utilizacao = Utilizacao(nadador, toalha, atendente_entrega)

                if not item.get("aberta", True):
                    utilizacao.aberta = False
                    atendente_dev = atendentes_dict.get(item.get("atendente_devolucao_nome"))
                    if atendente_dev:
                        utilizacao.atendente_devolucao = atendente_dev

                utilizacoes.append(utilizacao)

        return utilizacoes