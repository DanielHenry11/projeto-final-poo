class MenuUtilizacoes:

    def __init__(self, sistema):
        self.sistema = sistema

    def executar(self):

        while True:

            print("\n===== UTILIZAÇÕES =====")
            print("1 - Registrar retirada")
            print("2 - Registrar devolução")
            print("3 - Utilizações abertas")
            print("4 - Histórico")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":

                matricula = input("Matrícula: ")
                codigo = input("Código da toalha: ")
                atendente = input("Nome do atendente: ")

                self.sistema.retirar(
                    matricula,
                    codigo,
                    atendente
                )

            elif opcao == "2":

                codigo = input("Código da toalha: ")
                atendente = input("Nome do atendente: ")

                self.sistema.devolver(
                    codigo,
                    atendente
                )

            elif opcao == "3":

                encontrou = False

                for utilizacao in self.sistema.utilizacoes:

                    if utilizacao.aberta:

                        print(
                            "Toalha:",
                            utilizacao.toalha.codigo
                        )

                        print(
                            "Nadador:",
                            utilizacao.nadador.nome
                        )

                        print(
                            "Atendente:",
                            utilizacao.atendente_entrega.nome
                        )

                        print("--------------------")

                        encontrou = True

                if not encontrou:
                    print("Nenhuma utilização aberta.")

            elif opcao == "4":

                if len(self.sistema.utilizacoes) == 0:
                    print("Nenhuma utilização registrada.")

                else:

                    for utilizacao in self.sistema.utilizacoes:

                        if utilizacao.aberta:
                            estado = "ABERTA"
                        else:
                            estado = "ENCERRADA"

                        print(
                            "Toalha:",
                            utilizacao.toalha.codigo
                        )

                        print(
                            "Nadador:",
                            utilizacao.nadador.nome
                        )

                        print(
                            "Atendente da entrega:",
                            utilizacao.atendente_entrega.nome
                        )

                        if utilizacao.atendente_devolucao is not None:
                            print(
                                "Atendente da devolução:",
                                utilizacao.atendente_devolucao.nome
                            )

                        print("Estado:", estado)
                        print("--------------------")

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")