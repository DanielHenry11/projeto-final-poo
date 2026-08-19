class MenuNadadores:

    def __init__(self, sistema):
        self.sistema = sistema

    def executar(self):

        while True:

            print("\n===== NADADORES =====")
            print("1 - Cadastrar nadador")
            print("2 - Listar nadadores")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":

                nome = input("Nome: ")
                matricula = input("Matrícula: ")

                self.sistema.cadastrar_nadador(
                    nome,
                    matricula
                )

                print("Nadador cadastrado.")

            elif opcao == "2":

                if len(self.sistema.nadadores) == 0:
                    print("Nenhum nadador cadastrado.")
                else:

                    print("\n--- NADADORES ---")

                    for nadador in self.sistema.nadadores:
                        print(
                            "Nome:",
                            nadador.nome,
                            "| Matrícula:",
                            nadador.matricula
                        )

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")