# 🏊‍♂️ SwimTowel Manager — Sistema de Gestão de Toalhas

Este projeto é um sistema desenvolvido em Python para a disciplina de Programação Orientada a Objetos (POO). O seu objetivo principal é gerir o empréstimo e a devolução de toalhas para nadadores, contando com o suporte dos atendentes.

O sistema utiliza uma arquitetura organizada em camadas, separando as entidades de domínio, os serviços com as regras de negócio, as telas de interface no terminal e a camada de persistência. 

Todos os dados cadastrados (nadadores, atendentes, toalhas e o histórico de utilizações) são gravados automaticamente em ficheiros no formato JSON na pasta `dados` ao fechar o programa, sendo reconstruídos na memória assim que a aplicação é iniciada novamente através do ficheiro `main.py`.

---

## 👥 Identificação da Equipe
- **Nome do Projeto:** Sistema de Controle e Gestão de Toalhas (SwimTowel Manager)
- **Integrantes da Equipe:**
  * Daniel Henry
  * Luiz Guilherme Costa
  * Igor Gabriel Militão
- **Estudo de Caso:** Controle de empréstimo, devolução e enxoval de toalhas para escola de natação.
- **Repositório:** [github.com/DanielHenry11/projeto-final-poo](https://github.com/DanielHenry11/projeto-final-poo)

---

## 🗄️ Implementação do Banco de Dados Relacional

- **SGBD Utilizado:** MySQL 8.0 / MariaDB
- **Nome do Banco:** `swim_towel_manager`
- **Quantidade de Tabelas:** 5 (`atendente`, `nadador`, `toalha`, `retirada`, `historico_toalha`)
- **Massa de Testes Total:** 1.000 registros

### Distribuição dos Registros
| Tabela | Qtd. Registros | Papel no Sistema |
|---|---|---|
| `atendente` | 10 | Funcionários que gerenciam os empréstimos |
| `nadador` | 150 | Alunos cadastrados no estabelecimento |
| `toalha` | 240 | Itens do enxoval monitorados por código de barras |
| `retirada` | 300 | Registros de retiradas e devoluções |
| `historico_toalha` | 300 | Eventos de auditoria e movimentações do enxoval |
| **Total** | **1.000** | **Massa completa para testes** |

---

## 📁 Arquivos do Projeto

- `database.sql`: Script responsável por criar o banco de dados, definir tabelas com chaves primárias, chaves estrangeiras, restrições (`NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT`) e realizar a carga da massa de testes de 1.000 registros.
- `README.md`: Documentação atualizada do projeto.

---

## 🚀 Como Executar o Script

Para carregar o banco e a massa de dados em seu ambiente local:

```bash
mysql -u seu_usuario -p < database.sql