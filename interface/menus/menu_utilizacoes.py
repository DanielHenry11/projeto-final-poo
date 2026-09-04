from servicos.utilizacao_service import UtilizacaoService
from excecoes.nado_livre_error import NadoLivreError

class MenuUtilizacoes:
    def __init__(self, utilizacao_service: UtilizacaoService):
        self.utilizacao_service = utilizacao_service

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
                try:
                    self.utilizacao_service.retirar(matricula, codigo, atendente)
                    print("✅ Retirada realizada com sucesso.")
                except NadoLivreError as e:
                    print(f"⚠️ Erro: {e}")

            elif opcao == "2":
                codigo = input("Código da toalha: ")
                atendente = input("Nome do atendente: ")
                try:
                    self.utilizacao_service.devolver(codigo, atendente)
                    print("✅ Devolução realizada com sucesso.")
                except NadoLivreError as e:
                    print(f"⚠️ Erro: {e}")

            elif opcao == "3":
                abertas = self.utilizacao_service.listar_abertas()
                if not abertas:
                    print("Nenhuma utilização aberta.")
                else:
                    for u in abertas:
                        print("Toalha:", u.toalha.codigo)
                        print("Nadador:", u.nadador.nome)
                        print("Atendente:", u.atendente_entrega.nome)
                        print("--------------------")

            elif opcao == "4":
                todas = self.utilizacao_service.listar_todas()
                if not todas:
                    print("Nenhuma utilização registrada.")
                else:
                    for u in todas:
                        estado = "ABERTA" if u.aberta else "ENCERRADA"
                        print("Toalha:", u.toalha.codigo)
                        print("Nadador:", u.nadador.nome)
                        print("Atendente da entrega:", u.atendente_entrega.nome)
                        if u.atendente_devolucao:
                            print("Atendente da devolução:", u.atendente_devolucao.nome)
                        print("Estado:", estado)
                        print("--------------------")

            elif opcao == "0":
                break
            else:
                print("Opção inválida.")