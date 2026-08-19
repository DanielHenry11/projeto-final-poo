class MenuAtendentes:

    def __init__(self, sistema):
        self.sistema = sistema

    def executar(self):

     while True:

            print("\n===== ATENDENTES =====")
            print("1 - Cadastrar atendente")
            print("2 - Listar atendentes")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":

                nome = input("Nome: ")

                self.sistema.cadastrar_atendente(nome)

                print("Atendente cadastrado.")

            elif opcao == "2":

                if len(self.sistema.atendentes) == 0:
                    print("Nenhum atendente cadastrado.")
                else:

                    print("\n--- ATENDENTES ---")

                    for atendente in self.sistema.atendentes:
                        print("Nome:", atendente.nome)

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")