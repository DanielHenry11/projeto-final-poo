from src.dominio.modelos_base import Aluno, Professor, Toalha, Usuario
from src.excecoes.excecoes import (
    LimiteToalhasExcedidoException,
    RecursoNaoEncontradoException,
    ToalhaIndisponivelException,
)


class SistemaEscolaNatacao:
    """Gerenciador central do sistema em memória para a Versão 1."""

    def __init__(self) -> None:
        self.usuarios: list[Usuario] = []
        self.toalhas: list[Toalha] = []

    def cadastrar_usuario(self, usuario: Usuario) -> None:
        """Adiciona um utilizador ao sistema."""
        self.usuarios.append(usuario)

    def cadastrar_toalha(self, toalha: Toalha) -> None:
        """Adiciona uma toalha ao acervo."""
        self.toalhas.append(toalha)

    def buscar_usuario(self, id_usuario: int) -> Usuario:
        """Busca um utilizador pelo ID ou lança exceção."""
        for u in self.usuarios:
            if u.id_usuario == id_usuario:
                return u
        raise RecursoNaoEncontradoException(f"Utilizador com ID {id_usuario} não foi encontrado.")

    def buscar_toalha(self, id_toalha: int) -> Toalha:
        """Busca uma toalha pelo ID ou lança exceção."""
        for t in self.toalhas:
            if t.id_toalha == id_toalha:
                return t
        raise RecursoNaoEncontradoException(f"Toalha com ID {id_toalha} não foi encontrada.")

    def realizar_emprestimo(self, id_usuario: int, id_toalha: int) -> None:
        """Empresta uma toalha a um utilizador aplicando as regras de negócio."""
        usuario = self.buscar_usuario(id_usuario)
        toalha = self.buscar_toalha(id_toalha)

        if not toalha.disponivel:
            raise ToalhaIndisponivelException(f"A toalha ID {id_toalha} já está emprestada.")

        if usuario.toalhas_empossadas >= usuario.limite_maximo_toalhas():
            raise LimiteToalhasExcedidoException(
                f"O utilizador {usuario.nome} atingiu o limite de {usuario.limite_maximo_toalhas()} toalha(s)."
            )

        toalha.disponivel = False
        usuario.incrementar_toalhas()

    def realizar_devolucao(self, id_usuario: int, id_toalha: int) -> None:
        """Devolve uma toalha ao acervo."""
        usuario = self.buscar_usuario(id_usuario)
        toalha = self.buscar_toalha(id_toalha)

        if toalha.disponivel:
            raise ToalhaIndisponivelException(f"A toalha ID {id_toalha} já consta como disponível.")

        toalha.disponivel = True
        usuario.decrementar_toalhas()


def exibir_menu() -> None:
    """Exibe o menu textual e gerencia as interações no terminal."""
    sistema = SistemaEscolaNatacao()

    while True:
        print("\n=== SISTEMA DE CONTROLE DE TOALHAS ===")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Professor")
        print("3. Cadastrar Toalha")
        print("4. Emprestar Toalha")
        print("5. Devolver Toalha")
        print("6. Listar Usuários e Toalhas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                id_u = int(input("ID do Aluno: "))
                nome = input("Nome do Aluno: ")
                sistema.cadastrar_usuario(Aluno(id_u, nome))
                print("Aluno cadastrado com sucesso!")

            elif opcao == "2":
                id_u = int(input("ID do Professor: "))
                nome = input("Nome do Professor: ")
                sistema.cadastrar_usuario(Professor(id_u, nome))
                print("Professor cadastrado com sucesso!")

            elif opcao == "3":
                id_t = int(input("ID da Toalha: "))
                tamanho = input("Tamanho (P/M/G): ").strip().upper()
                sistema.cadastrar_toalha(Toalha(id_t, tamanho))
                print("Toalha cadastrada com sucesso!")

            elif opcao == "4":
                id_u = int(input("ID do Utilizador: "))
                id_t = int(input("ID da Toalha: "))
                sistema.realizar_emprestimo(id_u, id_t)
                print("Empréstimo realizado com sucesso!")

            elif opcao == "5":
                id_u = int(input("ID do Utilizador: "))
                id_t = int(input("ID da Toalha: "))
                sistema.realizar_devolucao(id_u, id_t)
                print("Devolução realizada com sucesso!")

            elif opcao == "6":
                print("\n--- UTILIZADORES ---")
                for u in sistema.usuarios:
                    tipo = "Aluno" if isinstance(u, Aluno) else "Professor"
                    print(f"[{tipo}] ID: {u.id_usuario} | Nome: {u.nome} | Toalhas em posse: {u.toalhas_empossadas}/{u.limite_maximo_toalhas()}")

                print("\n--- TOALHAS ---")
                for t in sistema.toalhas:
                    status = "Disponível" if t.disponivel else "Emprestada"
                    print(f"ID: {t.id_toalha} | Tamanho: {t.tamanho} | Status: {status}")

            elif opcao == "0":
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida! Tente novamente.")

        except ValueError:
            print("Erro: Digite apenas números inteiros para os IDs.")
        except Exception as e:
            print(f"Erro de negócio: {e}")