from servicos.toalha_service import ToalhaService
from servicos.utilizacao_service import UtilizacaoService
from excecoes.nado_livre_error import NadoLivreError

class MenuToalhas:
    def __init__(self, toalha_service: ToalhaService, utilizacao_service: UtilizacaoService):
        self.toalha_service = toalha_service
        self.utilizacao_service = utilizacao_service

    def executar(self) -> None:
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
                try:
                    self.toalha_service.cadastrar(codigo)
                    print("✅ Toalha cadastrada com sucesso.")
                except NadoLivreError as e:
                    print(f"⚠️ Erro: {e}")

            elif opcao == "2":
                toalhas = self.toalha_service.listar()
                if not toalhas:
                    print("Nenhuma toalha cadastrada.")
                else:
                    for toalha in toalhas:
                        estado = "Disponível" if toalha.disponivel else "Em uso"
                        print(f"Código: {toalha.codigo} | Estado: {estado}")

            elif opcao == "3":
                disponiveis = self.toalha_service.listar_disponiveis()
                if not disponiveis:
                    print("Nenhuma toalha disponível.")
                else:
                    for toalha in disponiveis:
                        print(f"Código: {toalha.codigo}")

            elif opcao == "4":
                em_uso = self.utilizacao_service.listar_abertas()
                if not em_uso:
                    print("Nenhuma toalha em uso.")
                else:
                    for utilizacao in em_uso:
                        print(f"Toalha: {utilizacao.toalha.codigo} | Nadador: {utilizacao.nadador.nome}")

            elif opcao == "0":
                break
            else:
                print("Opção inválida.")