from nado_livre import NadoLivre
from servicos.nadador_service import NadadorService
from servicos.atendente_service import AtendenteService
from servicos.toalha_service import ToalhaService
from servicos.utilizacao_service import UtilizacaoService

from interface.menus.menu_nadadores import MenuNadadores
from interface.menus.menu_atendentes import MenuAtendentes
from interface.menus.menu_toalhas import MenuToalhas
from interface.menus.menu_utilizacoes import MenuUtilizacoes

class MenuPrincipal:
    def __init__(self, sistema: NadoLivre) -> None:
        self.nadador_service = NadadorService(sistema)
        self.atendente_service = AtendenteService(sistema)
        self.toalha_service = ToalhaService(sistema)
        self.utilizacao_service = UtilizacaoService(sistema)

    def executar(self) -> None:
        menu_nadadores = MenuNadadores(self.nadador_service)
        menu_atendentes = MenuAtendentes(self.atendente_service)
        menu_toalhas = MenuToalhas(self.toalha_service, self.utilizacao_service)
        menu_utilizacoes = MenuUtilizacoes(self.utilizacao_service)

        while True:
            print("\n===== NADO LIVRE =====")
            print("1 - Nadadores")
            print("2 - Atendentes")
            print("3 - Toalhas")
            print("4 - Utilizações")
            print("0 - Sair")

            opcao = input("Opção: ")

            if opcao == "1":
                menu_nadadores.executar()
            elif opcao == "2":
                menu_atendentes.executar()
            elif opcao == "3":
                menu_toalhas.executar()
            elif opcao == "4":
                menu_utilizacoes.executar()
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")