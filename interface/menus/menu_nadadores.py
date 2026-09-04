from servicos.nadador_service import NadadorService
from excecoes.nado_livre_error import NadoLivreError

class MenuNadadores:
    def __init__(self, nadador_service: NadadorService) -> None:
        self.nadador_service = nadador_service

    def executar(self) -> None:
        while True:
            print("\n===== NADADORES =====")
            print("1 - Cadastrar nadador")
            print("2 - Listar nadadores")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":
                nome = input("Nome: ")
                matricula = input("Matrícula: ")
                try:
                    self.nadador_service.cadastrar(nome, matricula)
                    print("✅ Nadador cadastrado com sucesso.")
                except NadoLivreError as e:
                    print(f"⚠️ Erro: {e}")

            elif opcao == "2":
                nadadores = self.nadador_service.listar()
                if not nadadores:
                    print("Nenhum nadador cadastrado.")
                else:
                    print("\n--- NADADORES ---")
                    for nadador in nadadores:
                        print(f"Nome: {nadador.nome} | Matrícula: {nadador.matricula}")

            elif opcao == "0":
                break
            else:
                print("Opção inválida.")