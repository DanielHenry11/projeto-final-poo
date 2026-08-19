from interface.menus.menu_nadadores import MenuNadadores
from interface.menus.menu_atendentes import MenuAtendentes
from interface.menus.menu_toalhas import MenuToalhas
from interface.menus.menu_utilizacoes import MenuUtilizacoes


class MenuPrincipal:

    def __init__(self, sistema):
        self.sistema = sistema

    def executar(self):

        menu_nadadores = MenuNadadores(self.sistema)
        menu_atendentes = MenuAtendentes(self.sistema)
        menu_toalhas = MenuToalhas(self.sistema)
        menu_utilizacoes = MenuUtilizacoes(self.sistema)

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