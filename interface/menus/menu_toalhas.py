class MenuToalhas:

    def __init__(self, sistema):
        self.sistema = sistema

    def executar(self):

        while True:

            print("\n===== TOALHAS =====")
            print("1 - Cadastrar toalha")
            print("2 - Listar toalhas")
            print("3 - Toalhas disponíveis")
            print("4 - Toalhas em uso")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":

                codigo = input("Código da toalha: ")

                self.sistema.cadastrar_toalha(codigo)

                print("Toalha cadastrada.")

            elif opcao == "2":

                if len(self.sistema.toalhas) == 0:
                    print("Nenhuma toalha cadastrada.")
                else:

                    for toalha in self.sistema.toalhas:

                        if toalha.disponivel:
                            estado = "Disponível"
                        else:
                            estado = "Em uso"

                        print(
                            "Código:",
                            toalha.codigo,
                            "| Estado:",
                            estado
                        )

            elif opcao == "3":

                encontrou = False

                for toalha in self.sistema.toalhas:

                    if toalha.disponivel:
                        print(
                            "Código:",
                            toalha.codigo
                        )

                        encontrou = True

                if not encontrou:
                    print("Nenhuma toalha disponível.")

            elif opcao == "4":

                encontrou = False

                for utilizacao in self.sistema.utilizacoes:

                    if utilizacao.aberta:

                        print(
                            "Toalha:",
                            utilizacao.toalha.codigo,
                            "| Nadador:",
                            utilizacao.nadador.nome
                        )

                        encontrou = True

                if not encontrou:
                    print("Nenhuma toalha em uso.")

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")