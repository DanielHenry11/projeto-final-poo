from servicos.atendente_service import AtendenteService
from excecoes.nado_livre_error import NadoLivreError

class MenuAtendentes:
    def __init__(self, atendente_service: AtendenteService) -> None:
        self.atendente_service = atendente_service

    def executar(self) -> None:
        while True:
            print("\n===== ATENDENTES =====")
            print("1 - Cadastrar atendente")
            print("2 - Listar atendentes")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":
                nome = input("Nome: ")
                try:
                    self.atendente_service.cadastrar(nome)
                    print("✅ Atendente cadastrado com sucesso.")
                except NadoLivreError as e:
                    print(f"⚠️ Erro: {e}")

            elif opcao == "2":
                atendentes = self.atendente_service.listar()
                if not atendentes:
                    print("Nenhum atendente cadastrado.")
                else:
                    print("\n--- ATENDENTES ---")
                    for atendente in atendentes:
                        print(f"Nome: {atendente.nome}")

            elif opcao == "0":
                break
            else:
                print("Opção inválida.")